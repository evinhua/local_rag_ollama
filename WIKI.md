# 📚 Local RAG with Ollama - Project Wiki

## 🌟 **Project Overview**

**Local RAG with Ollama** is a comprehensive **Retrieval-Augmented Generation (RAG)** solution that runs entirely locally, ensuring complete privacy and security. This project combines modern web technologies with cutting-edge AI models to create an intelligent document analysis and question-answering system.

### 🎯 **Key Value Propositions**

- **🔒 100% Privacy**: All processing happens locally - no data leaves your machine
- **📄 Multi-format Support**: Handles PDF, DOCX, and PPTX documents seamlessly
- **🖼️ Multimodal Capabilities**: Supports both text and image queries
- **💬 Interactive Experience**: Real-time chat interface with conversation history
- **📊 Source Attribution**: Transparent sourcing shows which documents informed each answer
- **🚀 Production Ready**: Complete setup automation and comprehensive documentation

---

## 🏗️ **Architecture & Technology Stack**

### **System Architecture**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React App     │    │   FastAPI        │    │     Ollama      │
│   (Frontend)    │◄──►│   (Backend)      │◄──►│   (AI Models)   │
│                 │    │                  │    │                 │
│ • Chat UI       │    │ • Document Proc  │    │ • BGE-M3        │
│ • File Upload   │    │ • Vector Search  │    │ • Gemma3:4b     │
│ • Status Monitor│    │ • API Endpoints  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    ChromaDB     │
                       │ (Vector Store)  │
                       │                 │
                       │ • Embeddings    │
                       │ • Metadata      │
                       │ • Persistence   │
                       └─────────────────┘
```

### **Technology Stack**

#### **🤖 AI & Machine Learning**
- **Embedding Model**: BGE-M3 (multimodal embeddings for text and images)
- **Generation Model**: Gemma3:4b (efficient text generation)
- **Vector Database**: ChromaDB with cosine similarity search
- **Model Runtime**: Ollama (local inference engine)

#### **🐍 Backend Technologies**
- **Framework**: FastAPI with async support and automatic API documentation
- **Data Validation**: Pydantic models for type safety and validation
- **Document Processing**: 
  - PyPDF2 for PDF files
  - python-docx for Word documents
  - python-pptx for PowerPoint presentations
- **Image Processing**: Pillow (PIL) for image handling
- **Database**: ChromaDB for persistent vector storage

#### **⚛️ Frontend Technologies**
- **Framework**: React 18 with modern hooks and functional components
- **UI Components**: Lucide React icons for consistent iconography
- **File Upload**: react-dropzone for drag-and-drop functionality
- **Markdown Rendering**: react-markdown for formatted responses
- **HTTP Client**: Axios for API communication
- **Styling**: Modern CSS with responsive design

---

## 📁 **Project Structure**

```
local_rag_ollama/
├── 📄 README.md                    # Main project documentation
├── 📄 RAG_README.md                # Detailed usage guide
├── 📄 PROJECT_STRUCTURE.md         # Architecture documentation
├── 📄 TROUBLESHOOTING.md           # Common issues and solutions
├── 📄 CLEAR_CHAT_FEATURE.md        # Feature documentation
├── 📄 MODEL_UPDATE.md              # AI model configuration
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
│
├── 🔧 setup.sh                     # Automated setup script
├── 🚀 start_rag.sh                 # Application launcher
├── 🚀 start.sh                     # Alternative launcher
├── 🧪 test_setup.py                # Setup verification
├── 🧪 test_clear_chat.html         # Feature testing
│
├── 🐍 rag_backend/                 # Python FastAPI Backend
│   ├── 📄 main.py                  # FastAPI application entry
│   ├── 📄 models.py                # Pydantic data models
│   ├── 📄 rag_service.py           # Core RAG logic
│   ├── 📄 document_processor.py    # Document processing
│   ├── 📄 requirements.txt         # Python dependencies
│   ├── 📁 venv/                    # Virtual environment
│   ├── 📁 chroma_db/               # Vector database storage
│   ├── 📁 uploads/                 # Temporary file storage
│   └── 📁 __pycache__/             # Python cache
│
└── ⚛️ rag_frontend/                # React Frontend
    ├── 📄 package.json             # Node.js dependencies
    ├── 📄 package-lock.json        # Dependency lock file
    ├── 📁 public/
    │   └── 📄 index.html           # HTML template
    ├── 📁 src/
    │   ├── 📄 index.js             # React entry point
    │   ├── 📄 index.css            # Global styles
    │   ├── 📄 App.js               # Main application
    │   ├── 📄 App.css              # Application styles
    │   └── 📁 components/
    │       ├── 📄 DocumentUpload.js     # File upload component
    │       ├── 📄 DocumentUpload.css    # Upload styles
    │       ├── 📄 ChatInterface.js      # Chat component
    │       ├── 📄 ChatInterface.css     # Chat styles
    │       ├── 📄 StatusBar.js          # Status monitoring
    │       └── 📄 StatusBar.css         # Status styles
    └── 📁 node_modules/            # Node.js packages
```

---

## 🚀 **Getting Started**

### **Prerequisites**
- **Ollama**: Download from [ollama.ai](https://ollama.ai)
- **Python 3.8+**: For backend services
- **Node.js 16+**: For frontend development
- **6GB+ RAM**: Recommended for optimal performance

### **Quick Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/evinhua/local_rag_ollama.git
   cd local_rag_ollama
   ```

2. **Run Automated Setup**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   
   This script will:
   - Verify Ollama installation
   - Pull required AI models (BGE-M3, Gemma3:4b)
   - Set up Python virtual environment
   - Install all backend dependencies
   - Install all frontend dependencies

3. **Start the Application**
   ```bash
   chmod +x start_rag.sh
   ./start_rag.sh
   ```

4. **Access the Application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

---

## 💡 **Core Features & Capabilities**

### **📄 Document Processing**
- **Supported Formats**: PDF, DOCX, PPTX
- **Intelligent Chunking**: Optimized text segmentation for better retrieval
- **Metadata Extraction**: Preserves document structure and context
- **Batch Processing**: Handle multiple documents simultaneously

### **🔍 Semantic Search**
- **Vector Embeddings**: BGE-M3 model for high-quality embeddings
- **Similarity Search**: Cosine similarity for relevant chunk retrieval
- **Context Assembly**: Intelligent context building from multiple sources
- **Source Attribution**: Track which documents contributed to answers

### **💬 Interactive Chat Interface**
- **Real-time Responses**: Streaming responses for better UX
- **Conversation History**: Persistent chat sessions
- **Multimodal Input**: Text and image query support
- **Clear Chat Feature**: Easy conversation reset
- **Markdown Support**: Rich text formatting in responses

### **🖼️ Multimodal Capabilities**
- **Image Upload**: Support for various image formats
- **Visual Question Answering**: Combine text and image context
- **Cross-modal Retrieval**: Find relevant text based on image queries

### **📊 System Monitoring**
- **Health Checks**: Real-time system status monitoring
- **Service Status**: Ollama and ChromaDB connectivity
- **Performance Metrics**: Response times and system resources
- **Error Handling**: Comprehensive error reporting and recovery

---

## 🔧 **API Reference**

### **Document Management Endpoints**

#### `POST /upload`
Upload and process documents for RAG system.

**Request**: Multipart form data with file
**Response**: 
```json
{
  "success": true,
  "message": "Document processed successfully",
  "document_id": "uuid-string",
  "chunks_created": 15
}
```

#### `GET /documents`
Retrieve list of all uploaded documents.

**Response**:
```json
{
  "documents": [
    {
      "id": "uuid-string",
      "filename": "document.pdf",
      "upload_time": "2024-01-01T12:00:00Z",
      "chunks": 15
    }
  ]
}
```

#### `DELETE /documents`
Clear all uploaded documents and reset vector database.

**Response**:
```json
{
  "success": true,
  "message": "All documents cleared"
}
```

### **Chat Endpoints**

#### `POST /chat`
Send chat message with optional image for multimodal queries.

**Request**:
```json
{
  "message": "What is the main topic of the uploaded documents?",
  "image": "base64-encoded-image-data" // optional
}
```

**Response**:
```json
{
  "response": "Based on the uploaded documents...",
  "sources": [
    {
      "document": "document.pdf",
      "chunk": "relevant text chunk",
      "similarity": 0.85
    }
  ]
}
```

### **System Endpoints**

#### `GET /health`
Check system health and service status.

**Response**:
```json
{
  "status": "healthy",
  "ollama_status": "connected",
  "chroma_status": "connected",
  "models": {
    "embedding": "bge-m3:latest",
    "generation": "gemma3:4b"
  }
}
```

---

## 🔒 **Privacy & Security**

### **Local Processing Guarantee**
- **No External Calls**: All AI inference happens locally via Ollama
- **Data Isolation**: Documents never leave your machine
- **Network Independence**: Works completely offline after setup
- **Secure by Design**: No telemetry or data collection

### **Security Features**
- **Input Validation**: Pydantic models ensure data integrity
- **File Type Validation**: Strict file format checking
- **CORS Protection**: Restricted to localhost origins
- **Temporary Storage**: Uploaded files cleaned automatically
- **Error Sanitization**: No sensitive data in error messages

---

## 📊 **Performance & Optimization**

### **System Requirements**
- **Memory**: 5-6GB RAM (models + application)
- **Storage**: ~4GB for AI models, minimal for documents
- **CPU**: Multi-core recommended for faster processing
- **GPU**: Optional, Ollama can utilize CUDA if available

### **Performance Characteristics**
- **Response Time**: 2-5 seconds depending on hardware
- **Document Size**: Up to 50MB per document recommended
- **Concurrent Users**: Single-user design, can be extended
- **Scalability**: Horizontal scaling possible with load balancer

### **Optimization Features**
- **Embedding Caching**: ChromaDB persists embeddings
- **Chunking Strategy**: 500-1000 token chunks with overlap
- **Model Efficiency**: Using 4B parameter model for balance
- **Memory Management**: Automatic cleanup of temporary files

---

## 🛠️ **Development & Customization**

### **Backend Customization**
- **Model Selection**: Easy switching between Ollama models
- **Chunking Strategy**: Configurable text segmentation
- **Embedding Dimensions**: Adjustable vector dimensions
- **API Extensions**: FastAPI makes adding endpoints simple

### **Frontend Customization**
- **UI Components**: Modular React components
- **Styling**: CSS modules for easy theming
- **Feature Toggles**: Enable/disable features via configuration
- **Responsive Design**: Mobile-friendly interface

### **Configuration Options**
- **Model Parameters**: Temperature, max tokens, etc.
- **Retrieval Settings**: Number of chunks, similarity threshold
- **UI Preferences**: Theme, layout, component visibility
- **Performance Tuning**: Batch sizes, timeout values

---

## 🧪 **Testing & Quality Assurance**

### **Testing Features**
- **Health Checks**: Automated system status verification
- **Setup Validation**: `test_setup.py` verifies installation
- **Feature Testing**: `test_clear_chat.html` for UI testing
- **Error Handling**: Comprehensive error scenarios covered

### **Quality Measures**
- **Type Safety**: Pydantic models for data validation
- **Error Boundaries**: Graceful error handling throughout
- **Logging**: Detailed application logging for debugging
- **Documentation**: Comprehensive inline and external docs

---

## 🤝 **Contributing & Community**

### **Contributing Guidelines**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Development Setup**
```bash
# Clone your fork
git clone https://github.com/yourusername/local_rag_ollama.git
cd local_rag_ollama

# Set up development environment
./setup.sh

# Start development servers
./start_rag.sh
```

### **Code Standards**
- **Python**: Follow PEP 8 style guidelines
- **JavaScript**: Use ESLint and Prettier for formatting
- **Documentation**: Update docs for any new features
- **Testing**: Add tests for new functionality

---

## 📈 **Use Cases & Applications**

### **Personal Knowledge Management**
- **Document Analysis**: Analyze personal documents and research papers
- **Note Organization**: Create searchable knowledge bases
- **Research Assistant**: Get insights from multiple sources
- **Content Summarization**: Extract key points from large documents

### **Professional Applications**
- **Legal Document Review**: Analyze contracts and legal documents
- **Academic Research**: Process research papers and publications
- **Business Intelligence**: Analyze reports and presentations
- **Technical Documentation**: Search through technical manuals

### **Educational Use**
- **Study Assistant**: Ask questions about textbooks and materials
- **Research Projects**: Analyze multiple sources for projects
- **Literature Review**: Process academic papers efficiently
- **Knowledge Retention**: Create interactive study materials

---

## 🔮 **Future Roadmap**

### **Planned Features**
- **Multi-user Support**: User authentication and document isolation
- **Advanced Analytics**: Document insights and usage statistics
- **Export Capabilities**: Export conversations and insights
- **Plugin System**: Extensible architecture for custom processors
- **Cloud Deployment**: Docker containers and cloud deployment guides

### **Technical Improvements**
- **Performance Optimization**: Faster embedding and retrieval
- **Model Updates**: Support for newer and larger models
- **Database Scaling**: Distributed vector storage options
- **API Enhancements**: GraphQL support and advanced querying

---

## 📞 **Support & Resources**

### **Documentation**
- **[Main README](README.md)**: Project overview and quick start
- **[Detailed Guide](RAG_README.md)**: Comprehensive usage instructions
- **[Architecture](PROJECT_STRUCTURE.md)**: Technical architecture details
- **[Troubleshooting](TROUBLESHOOTING.md)**: Common issues and solutions

### **Community Support**
- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Ask questions and share ideas
- **Documentation**: Comprehensive guides and examples
- **Code Examples**: Well-documented codebase for learning

### **Technical Support**
- **System Requirements**: Detailed hardware and software requirements
- **Installation Help**: Step-by-step setup instructions
- **Configuration Guide**: Customization and optimization tips
- **Performance Tuning**: Hardware-specific optimization advice

---

## 📄 **License & Acknowledgments**

### **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **Acknowledgments**
- **[Ollama](https://ollama.ai)** - Local AI model runtime
- **[ChromaDB](https://www.trychroma.com/)** - Vector database solution
- **[BGE-M3](https://huggingface.co/BAAI/bge-m3)** - Multimodal embedding model
- **[Gemma](https://ai.google.dev/gemma)** - Text generation model
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[React](https://reactjs.org/)** - Frontend JavaScript library

---

## 🏷️ **Tags & Keywords**

`RAG` `Retrieval-Augmented-Generation` `Ollama` `Local-AI` `Privacy` `Document-Analysis` `Multimodal` `React` `FastAPI` `ChromaDB` `BGE-M3` `Gemma` `Python` `JavaScript` `Vector-Database` `Semantic-Search` `Question-Answering` `Knowledge-Management` `AI-Assistant` `Local-Processing`

---

**⭐ Star this repository if you find it useful!**

*Last updated: August 2024*
