import os
import uuid
import ollama
import chromadb
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from models import DocumentChunk, SearchResult, ChatRequest, ChatResponse
from document_processor import DocumentProcessor
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGService:
    def __init__(self):
        self.embedding_model_name = "bge-m3:latest"
        self.generation_model_name = "gemma3:4b"  # Using gemma3:4b as requested
        
        # Initialize Chroma client with telemetry disabled
        self.chroma_client = chromadb.PersistentClient(
            path="./chroma_db",
            settings=chromadb.Settings(anonymized_telemetry=False)
        )
        self.collection = self.chroma_client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
        
        # Initialize document processor
        self.doc_processor = DocumentProcessor()
        
        # Initialize embedding model (fallback to sentence-transformers if bge-m3 not available)
        try:
            # Try to use Ollama for embeddings
            self.use_ollama_embeddings = True
            self._test_ollama_embedding()
        except:
            logger.warning("BGE-M3 not available in Ollama, falling back to sentence-transformers")
            self.use_ollama_embeddings = False
            self.embedding_model = SentenceTransformer('BAAI/bge-m3')
    
    def _test_ollama_embedding(self):
        """Test if Ollama embedding model is available"""
        try:
            ollama.embeddings(model=self.embedding_model_name, prompt="test")
        except Exception as e:
            raise Exception(f"Ollama embedding model not available: {e}")
    
    def get_embedding(self, text: str) -> List[float]:
        """Generate embedding for text"""
        try:
            if self.use_ollama_embeddings:
                response = ollama.embeddings(model=self.embedding_model_name, prompt=text)
                return response['embedding']
            else:
                return self.embedding_model.encode(text).tolist()
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            # Fallback to sentence-transformers
            if not hasattr(self, 'embedding_model'):
                self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            return self.embedding_model.encode(text).tolist()
    
    def add_document(self, file_path: str, filename: str) -> Dict[str, Any]:
        """Process and add document to vector database"""
        try:
            # Process document
            chunks, file_type = self.doc_processor.process_document(file_path, filename)
            
            if not chunks:
                return {
                    "success": False,
                    "message": "No text content found in document",
                    "filename": filename,
                    "file_type": file_type
                }
            
            document_id = str(uuid.uuid4())
            
            # Generate embeddings and add to Chroma
            for i, chunk in enumerate(chunks):
                chunk_id = f"{document_id}_{i}"
                embedding = self.get_embedding(chunk)
                
                self.collection.add(
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{
                        "document_id": document_id,
                        "filename": filename,
                        "file_type": file_type,
                        "chunk_index": i,
                        "chunk_id": chunk_id
                    }],
                    ids=[chunk_id]
                )
            
            return {
                "success": True,
                "message": f"Document processed successfully",
                "document_id": document_id,
                "filename": filename,
                "file_type": file_type,
                "chunks_created": len(chunks)
            }
            
        except Exception as e:
            logger.error(f"Error adding document: {e}")
            return {
                "success": False,
                "message": f"Error processing document: {str(e)}",
                "filename": filename,
                "file_type": "unknown"
            }
    
    def search_documents(self, query: str, n_results: int = 5) -> List[SearchResult]:
        """Search for relevant documents"""
        try:
            query_embedding = self.get_embedding(query)
            
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            search_results = []
            if results['documents'] and results['documents'][0]:
                for i in range(len(results['documents'][0])):
                    search_results.append(SearchResult(
                        content=results['documents'][0][i],
                        metadata=results['metadatas'][0][i],
                        similarity_score=1 - results['distances'][0][i]  # Convert distance to similarity
                    ))
            
            return search_results
            
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []
    
    def generate_response(self, request: ChatRequest) -> ChatResponse:
        """Generate response using RAG"""
        try:
            # Search for relevant documents
            search_results = self.search_documents(request.message)
            
            # Prepare context from search results
            context = ""
            sources = []
            
            for result in search_results:
                context += f"Source: {result.metadata.get('filename', 'Unknown')}\n"
                context += f"Content: {result.content}\n\n"
                sources.append(result.metadata.get('filename', 'Unknown'))
            
            # Handle image if provided
            image_context = ""
            if request.image_data:
                image_info = self.doc_processor.process_image(request.image_data)
                image_context = f"User has uploaded an image: {image_info}\n"
            
            # Prepare conversation history
            history_context = ""
            for msg in request.conversation_history[-5:]:  # Last 5 messages
                history_context += f"{msg.role}: {msg.content}\n"
            
            # Create prompt
            prompt = f"""You are a helpful assistant that answers questions based on the provided context. 
            
Context from documents:
{context}

{image_context}

Previous conversation:
{history_context}

User question: {request.message}

Please provide a helpful and accurate answer based on the context provided. If the context doesn't contain relevant information, say so clearly."""

            # Generate response using Ollama
            response = ollama.chat(
                model=self.generation_model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return ChatResponse(
                response=response['message']['content'],
                sources=list(set(sources))  # Remove duplicates
            )
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return ChatResponse(
                response=f"I apologize, but I encountered an error while processing your request: {str(e)}",
                sources=[]
            )
    
    def health_check(self) -> Dict[str, str]:
        """Check the health of all services"""
        status = {
            "status": "healthy",
            "ollama_status": "unknown",
            "chroma_status": "unknown",
            "embedding_model": self.embedding_model_name,
            "generation_model": self.generation_model_name
        }
        
        # Check Ollama
        try:
            ollama.list()
            status["ollama_status"] = "healthy"
        except:
            status["ollama_status"] = "unhealthy"
            status["status"] = "degraded"
        
        # Check Chroma
        try:
            self.chroma_client.heartbeat()
            status["chroma_status"] = "healthy"
        except:
            status["chroma_status"] = "unhealthy"
            status["status"] = "degraded"
        
        return status
