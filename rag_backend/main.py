from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import aiofiles
import os
import tempfile
from pathlib import Path
import logging

from models import (
    DocumentUploadResponse, 
    ChatRequest, 
    ChatResponse, 
    HealthCheck
)
from rag_service import RAGService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Local RAG API",
    description="A local RAG solution with multimodal capabilities",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG service
rag_service = RAGService()

# Ensure upload directory exists
UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Local RAG API is running"}

@app.get("/health", response_model=HealthCheck)
async def health_check():
    """Health check endpoint"""
    try:
        health_status = rag_service.health_check()
        return HealthCheck(**health_status)
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=500, detail="Health check failed")

@app.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a document"""
    
    # Validate file type
    allowed_extensions = {'.pdf', '.docx', '.pptx'}
    file_extension = Path(file.filename).suffix.lower()
    
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file type. Allowed: {', '.join(allowed_extensions)}"
        )
    
    # Save uploaded file temporarily
    temp_file_path = None
    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            temp_file_path = temp_file.name
            
            # Write uploaded content to temp file
            content = await file.read()
            temp_file.write(content)
        
        # Process document with RAG service
        result = rag_service.add_document(temp_file_path, file.filename)
        
        return DocumentUploadResponse(**result)
        
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
    
    finally:
        # Clean up temporary file
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint with RAG capabilities"""
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        response = rag_service.generate_response(request)
        return response
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.delete("/documents")
async def clear_documents():
    """Clear all documents from the vector database"""
    try:
        # Delete the collection and recreate it
        rag_service.chroma_client.delete_collection("documents")
        rag_service.collection = rag_service.chroma_client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
        
        return {"message": "All documents cleared successfully"}
        
    except Exception as e:
        logger.error(f"Error clearing documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error clearing documents: {str(e)}")

@app.get("/documents")
async def list_documents():
    """List all documents in the database"""
    try:
        # Get all documents from collection
        results = rag_service.collection.get()
        
        # Extract unique documents
        documents = {}
        if results['metadatas']:
            for metadata in results['metadatas']:
                doc_id = metadata.get('document_id')
                if doc_id and doc_id not in documents:
                    documents[doc_id] = {
                        'document_id': doc_id,
                        'filename': metadata.get('filename'),
                        'file_type': metadata.get('file_type'),
                        'chunks': 0
                    }
                if doc_id:
                    documents[doc_id]['chunks'] += 1
        
        return {"documents": list(documents.values())}
        
    except Exception as e:
        logger.error(f"Error listing documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error listing documents: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
