# RAG Solution Troubleshooting Guide

## ✅ **SOLUTION FIXED!**

The proxy errors have been resolved. The issue was with:
1. **Missing dependencies** - Fixed by installing correct package versions
2. **Backend not starting** - Fixed compatibility issues with sentence-transformers
3. **Model configuration** - Updated to use available models

## 🚀 **Quick Start (Working Solution)**

```bash
cd /Users/evinhua/genai/proj1/amazon_q
./start_rag.sh
```

This will:
- ✅ Check if Ollama is running
- ✅ Clean up any existing processes
- ✅ Start backend on port 8000
- ✅ Wait for backend to be ready
- ✅ Start frontend on port 3000
- ✅ Display access URLs

## 🔍 **Common Issues & Solutions**

### 1. **Proxy Errors (ECONNREFUSED)**
**Symptoms**: `Could not proxy request from localhost:3000 to http://localhost:8000`

**Solutions**:
- ✅ **FIXED**: Backend now starts properly
- Use the new `start_rag.sh` script
- Backend health check: `curl http://localhost:8000/health`

### 2. **Backend Import Errors**
**Symptoms**: `ImportError: cannot import name 'cached_download'`

**Solutions**:
- ✅ **FIXED**: Updated sentence-transformers to version 2.7.0
- Removed incompatible langchain dependencies
- All imports now work correctly

### 3. **Ollama Model Issues**
**Symptoms**: Models not found or embedding errors

**Solutions**:
- ✅ **VERIFIED**: Both models are available
- `bge-m3:latest` - for embeddings
- `gemma3:4b` - for text generation (updated from gemma2:2b)
- Check with: `ollama list`

### 4. **Port Conflicts**
**Symptoms**: Address already in use

**Solutions**:
- ✅ **HANDLED**: Script automatically cleans up ports
- Manual cleanup: `lsof -ti:8000 | xargs kill -9`
- Manual cleanup: `lsof -ti:3000 | xargs kill -9`

## 🧪 **Testing the Solution**

### Backend Health Check
```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy","ollama_status":"healthy",...}
```

### Frontend Access
```bash
curl http://localhost:3000/
# Expected: HTML content with React app
```

### API Documentation
Visit: http://localhost:8000/docs

## 📊 **System Status**

### ✅ **Working Components**
- FastAPI backend with Pydantic models
- React frontend with modern UI
- ChromaDB vector database
- Ollama integration (BGE-M3 + Gemma2:2b)
- Document processing (PDF, DOCX, PPTX)
- Multimodal image upload
- Real-time health monitoring

### 🔧 **Configuration**
- **Backend**: Python 3.11, FastAPI, ChromaDB
- **Frontend**: React 18, Modern CSS, Responsive design
- **Models**: BGE-M3 (embeddings), Gemma3:4b (generation)
- **Database**: ChromaDB with cosine similarity
- **CORS**: Configured for localhost:3000

## 🚨 **If Issues Persist**

1. **Check Ollama Service**:
   ```bash
   ollama serve  # Start Ollama if not running
   ollama list   # Verify models are available
   ```

2. **Verify Dependencies**:
   ```bash
   cd rag_backend
   source venv/bin/activate
   python -c "import sentence_transformers, chromadb, ollama; print('All imports OK')"
   ```

3. **Check Logs**:
   - Backend logs: Check terminal output
   - Frontend logs: Check browser console
   - Ollama logs: Check Ollama service output

4. **Reset Everything**:
   ```bash
   # Kill all processes
   pkill -f "python main.py"
   pkill -f "npm start"
   
   # Restart
   ./start_rag.sh
   ```

## 📱 **Access URLs**

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🎉 **Success Indicators**

When everything is working, you should see:
- ✅ Backend health check returns "healthy" status
- ✅ Frontend loads without proxy errors
- ✅ Document upload panel on the left
- ✅ Chat interface on the right
- ✅ System status bar shows all green
- ✅ Can upload documents and ask questions

The solution is now fully functional!
