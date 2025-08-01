# Local RAG Solution

A comprehensive local Retrieval-Augmented Generation (RAG) solution with multimodal capabilities, built with React frontend and Python backend.

## Features

### 🚀 Core Capabilities
- **Document Processing**: Support for PDF, DOCX, and PPTX files
- **Multimodal Input**: Text and image queries
- **Local Processing**: Everything runs locally for privacy
- **Real-time Chat**: Interactive chat interface with conversation history
- **Source Attribution**: Shows which documents were used for answers

### 🛠 Technology Stack
- **Frontend**: React with modern UI components
- **Backend**: FastAPI with Pydantic data validation
- **Vector Database**: ChromaDB for document storage and retrieval
- **Embeddings**: BGE-M3 model via Ollama
- **Generation**: Gemma3:4b model via Ollama
- **Document Processing**: Custom processors for multiple formats

## Prerequisites

1. **Ollama**: Install from [https://ollama.ai](https://ollama.ai)
2. **Python 3.8+**: For the backend
3. **Node.js 16+**: For the React frontend

## Quick Start

### 1. Setup
```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Pull required Ollama models (bge-m3:latest, gemma3:4b)
- Set up Python virtual environment
- Install all dependencies

### 2. Start the Application
```bash
chmod +x start.sh
./start.sh
```

Or start services manually:

**Backend:**
```bash
cd rag_backend
source venv/bin/activate
python main.py
```

**Frontend:**
```bash
cd rag_frontend
npm start
```

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Usage Guide

### Document Upload
1. Drag and drop or click to select documents (.pdf, .docx, .pptx)
2. Documents are automatically processed and chunked
3. View uploaded documents in the left panel

### Chat Interface
1. Type questions about your uploaded documents
2. Upload images for multimodal queries
3. View sources used for each answer
4. Conversation history is maintained
5. **Clear Chat**: Use the "Clear Chat" button to start fresh conversations

### System Status
- Monitor Ollama and ChromaDB health in the status bar
- Refresh status manually if needed

## API Endpoints

### Document Management
- `POST /upload` - Upload and process documents
- `GET /documents` - List all uploaded documents
- `DELETE /documents` - Clear all documents

### Chat
- `POST /chat` - Send chat messages with optional images

### System
- `GET /health` - Check system health
- `GET /` - API status

## Architecture

### Backend Structure
```
rag_backend/
├── main.py              # FastAPI application
├── models.py            # Pydantic data models
├── rag_service.py       # Core RAG logic
├── document_processor.py # Document processing utilities
└── requirements.txt     # Python dependencies
```

### Frontend Structure
```
rag_frontend/
├── src/
│   ├── components/
│   │   ├── DocumentUpload.js    # Document upload panel
│   │   ├── ChatInterface.js     # Chat interface
│   │   └── StatusBar.js         # System status display
│   ├── App.js           # Main application
│   └── index.js         # React entry point
└── package.json         # Node.js dependencies
```

## Configuration

### Ollama Models
- **Embedding Model**: `bge-m3:latest` (multimodal embeddings)
- **Generation Model**: `gemma3:4b` (text generation)

You can modify these in `rag_service.py`:
```python
self.embedding_model_name = "bge-m3:latest"
self.generation_model_name = "gemma3:4b"
```

### ChromaDB
- Database stored in `./chroma_db`
- Uses cosine similarity for vector search
- Persistent storage across restarts

## Troubleshooting

### Common Issues

1. **Ollama Models Not Found**
   ```bash
   ollama pull bge-m3:latest
   ollama pull gemma3:4b
   ```

2. **Port Already in Use**
   - Backend (8000): Change port in `main.py`
   - Frontend (3000): Set `PORT=3001 npm start`

3. **Memory Issues**
   - Use smaller models like `gemma2:2b` instead of `gemma3:4b` if memory is limited
   - Reduce chunk size in document processing

4. **CORS Issues**
   - Ensure backend allows frontend origin in CORS settings

### Performance Optimization

1. **GPU Acceleration**: Ensure Ollama uses GPU if available
2. **Batch Processing**: Process multiple documents together
3. **Caching**: Embeddings are cached in ChromaDB
4. **Model Selection**: Choose appropriate model sizes for your hardware

## Development

### Adding New Document Types
1. Extend `DocumentProcessor` class
2. Add new file extensions to supported formats
3. Update frontend file type validation

### Custom Models
1. Pull new models with Ollama
2. Update model names in `rag_service.py`
3. Test compatibility with your use case

### UI Customization
- Modify CSS files in `src/components/`
- Update color scheme in CSS variables
- Add new components as needed

## Security Considerations

- All processing happens locally
- No data sent to external services
- Documents stored locally in ChromaDB
- Consider encryption for sensitive documents

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## License

This project is open source. See LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Check Ollama and ChromaDB documentation
4. Create an issue with detailed error information
