# Local RAG Solution - Project Structure

## 📁 Directory Layout

```
amazon_q/
├── 📄 RAG_README.md           # Main documentation
├── 📄 PROJECT_STRUCTURE.md    # This file
├── 🔧 setup.sh               # Setup script
├── 🚀 start.sh               # Start script  
├── 🧪 test_setup.py          # Setup verification
│
├── 🐍 rag_backend/           # Python FastAPI Backend
│   ├── 📄 main.py            # FastAPI application entry point
│   ├── 📄 models.py          # Pydantic data models
│   ├── 📄 rag_service.py     # Core RAG logic and services
│   ├── 📄 document_processor.py # Document processing utilities
│   ├── 📄 requirements.txt   # Python dependencies
│   ├── 📁 venv/              # Python virtual environment (created by setup)
│   ├── 📁 chroma_db/         # ChromaDB storage (created at runtime)
│   └── 📁 uploads/           # Temporary file uploads (created at runtime)
│
└── ⚛️  rag_frontend/          # React Frontend
    ├── 📄 package.json       # Node.js dependencies
    ├── 📁 public/
    │   └── 📄 index.html     # HTML template
    ├── 📁 src/
    │   ├── 📄 index.js       # React entry point
    │   ├── 📄 index.css      # Global styles
    │   ├── 📄 App.js         # Main React component
    │   ├── 📄 App.css        # Main app styles
    │   └── 📁 components/
    │       ├── 📄 DocumentUpload.js    # Document upload panel
    │       ├── 📄 DocumentUpload.css   # Upload panel styles
    │       ├── 📄 ChatInterface.js     # Chat interface
    │       ├── 📄 ChatInterface.css    # Chat interface styles
    │       ├── 📄 StatusBar.js         # System status bar
    │       └── 📄 StatusBar.css        # Status bar styles
    └── 📁 node_modules/      # Node.js packages (created by npm install)
```

## 🔧 Key Components

### Backend Components

#### `main.py`
- FastAPI application setup
- CORS configuration
- API endpoints definition
- File upload handling

#### `models.py`
- Pydantic models for data validation
- Request/response schemas
- Type definitions

#### `rag_service.py`
- Core RAG functionality
- Ollama integration
- ChromaDB operations
- Document embedding and retrieval

#### `document_processor.py`
- PDF, DOCX, PPTX processing
- Text chunking strategies
- Image processing utilities

### Frontend Components

#### `App.js`
- Main application layout
- State management
- Component orchestration

#### `DocumentUpload.js`
- Drag-and-drop file upload
- Document list display
- Upload status feedback

#### `ChatInterface.js`
- Chat message display
- Image upload for queries
- Conversation history
- Markdown rendering

#### `StatusBar.js`
- System health monitoring
- Service status indicators
- Refresh functionality

## 🚀 Getting Started

1. **Prerequisites Check**:
   ```bash
   python3 test_setup.py
   ```

2. **Setup Environment**:
   ```bash
   ./setup.sh
   ```

3. **Start Application**:
   ```bash
   ./start.sh
   ```

## 🔄 Data Flow

1. **Document Upload**:
   - User uploads document via React frontend
   - FastAPI receives file and saves temporarily
   - Document processor extracts and chunks text
   - RAG service generates embeddings
   - Chunks stored in ChromaDB with metadata

2. **Chat Query**:
   - User sends text/image query via React
   - FastAPI receives chat request
   - RAG service generates query embedding
   - ChromaDB searches for similar document chunks
   - Context assembled from retrieved chunks
   - Ollama generates response using context
   - Response sent back to React frontend

## 🛠 Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation and serialization
- **ChromaDB**: Vector database for embeddings
- **Ollama**: Local LLM inference
- **sentence-transformers**: Embedding models
- **PyPDF2, python-docx, python-pptx**: Document processing

### Frontend
- **React**: UI framework
- **react-dropzone**: File upload component
- **react-markdown**: Markdown rendering
- **lucide-react**: Icon library
- **axios**: HTTP client

### AI Models
- **BGE-M3**: Multimodal embedding model
- **Gemma2:2b**: Text generation model

## 📊 Performance Considerations

- **Chunking Strategy**: 500-1000 token chunks with overlap
- **Embedding Caching**: ChromaDB persists embeddings
- **Model Size**: Using 2B parameter model for efficiency
- **Batch Processing**: Multiple documents processed together
- **Memory Management**: Temporary files cleaned up automatically

## 🔒 Security Features

- **Local Processing**: No external API calls
- **File Validation**: Strict file type checking
- **Temporary Storage**: Uploaded files deleted after processing
- **CORS Protection**: Frontend-only access allowed
- **Input Sanitization**: Pydantic model validation

## 🧪 Testing

- **Health Checks**: System status monitoring
- **Error Handling**: Comprehensive error responses
- **Validation**: Input/output data validation
- **Logging**: Detailed application logging

## 📈 Scalability

- **Horizontal**: Multiple backend instances possible
- **Vertical**: Supports larger models with more resources
- **Storage**: ChromaDB scales with document volume
- **Caching**: Embedding reuse reduces computation
