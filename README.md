# 🤖 Local RAG with Ollama

A comprehensive **Retrieval-Augmented Generation (RAG)** solution that runs entirely locally for complete privacy and security. Built with React frontend and Python backend, powered by Ollama AI models.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![React](https://img.shields.io/badge/react-18.2+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)

## ✨ Features

- 🔒 **100% Local Processing** - No data leaves your machine
- 📄 **Multi-format Support** - PDF, DOCX, PPTX documents
- 🖼️ **Multimodal Queries** - Text + image input support
- 💬 **Real-time Chat** - Interactive interface with conversation history
- 🗑️ **Clear Chat** - Easy conversation reset functionality
- 📊 **Source Attribution** - See which documents informed each answer
- 🔍 **Semantic Search** - Advanced vector-based document retrieval
- 📱 **Responsive Design** - Works on desktop and mobile

## 🚀 Quick Start

### Prerequisites
- [Ollama](https://ollama.ai) installed and running
- Python 3.8+
- Node.js 16+
- 6GB+ RAM recommended

### Installation

```bash
# Clone the repository
git clone https://github.com/evinhua/local_rag_ollama.git
cd local_rag_ollama

# Run setup script (installs dependencies and pulls AI models)
chmod +x setup.sh
./setup.sh

# Start the application
chmod +x start_rag.sh
./start_rag.sh
```

### Access Points
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🛠️ Technology Stack

### AI & ML
- **Embedding Model**: BGE-M3 (multimodal embeddings)
- **Generation Model**: Gemma3:4b (text generation)
- **Vector Database**: ChromaDB with cosine similarity
- **Model Runtime**: Ollama (local inference)

### Backend
- **Framework**: FastAPI with Pydantic validation
- **Document Processing**: PyPDF2, python-docx, python-pptx
- **Image Processing**: Pillow
- **Database**: ChromaDB (persistent vector storage)

### Frontend
- **Framework**: React 18 with modern hooks
- **UI Components**: Lucide React icons
- **File Upload**: react-dropzone
- **Markdown**: react-markdown
- **HTTP Client**: Axios

## 📖 Documentation

- **[Complete Guide](RAG_README.md)** - Detailed setup and usage instructions
- **[Project Structure](PROJECT_STRUCTURE.md)** - Architecture and component overview
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions
- **[Clear Chat Feature](CLEAR_CHAT_FEATURE.md)** - New feature documentation
- **[Model Updates](MODEL_UPDATE.md)** - AI model configuration changes

## 🎯 Use Cases

- **Document Q&A**: Ask questions about your personal documents
- **Research Assistant**: Analyze multiple documents simultaneously
- **Content Summarization**: Extract key insights from large documents
- **Knowledge Base**: Build searchable collections of information
- **Multimodal Analysis**: Combine text queries with image context

## 🔧 Architecture

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

## 🔒 Privacy & Security

- **Local Processing**: All AI inference happens on your machine
- **No External Calls**: No data sent to third-party services
- **Document Privacy**: Files processed and stored locally only
- **Secure by Design**: CORS protection and input validation

## 📊 Performance

- **Memory Usage**: ~5-6GB RAM (models + application)
- **Storage**: ~4GB for AI models, minimal for documents
- **Response Time**: 2-5 seconds depending on hardware
- **Supported Files**: Up to 50MB per document recommended

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for local AI model runtime
- [ChromaDB](https://www.trychroma.com/) for vector database
- [BGE-M3](https://huggingface.co/BAAI/bge-m3) for multimodal embeddings
- [Gemma](https://ai.google.dev/gemma) for text generation
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [React](https://reactjs.org/) for the frontend framework

## 📞 Support

- 📖 Check the [documentation](RAG_README.md) first
- 🐛 Report issues on [GitHub Issues](https://github.com/evinhua/local_rag_ollama/issues)
- 💬 Start a [Discussion](https://github.com/evinhua/local_rag_ollama/discussions) for questions

---

**⭐ Star this repository if you find it useful!**
