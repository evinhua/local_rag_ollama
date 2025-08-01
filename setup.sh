#!/bin/bash

echo "🚀 Setting up Local RAG Solution..."

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed. Please install Ollama first:"
    echo "   Visit: https://ollama.ai"
    exit 1
fi

echo "✅ Ollama found"

# Pull required models
echo "📥 Pulling Ollama models..."
echo "   Pulling embedding model: bge-m3:latest"
ollama pull bge-m3:latest

echo "   Pulling generation model: gemma3:4b"
ollama pull gemma3:4b

# Setup backend
echo "🐍 Setting up Python backend..."
cd rag_backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "✅ Backend setup complete"

# Setup frontend
echo "⚛️  Setting up React frontend..."
cd ../rag_frontend

# Install npm dependencies
npm install

echo "✅ Frontend setup complete"

cd ..

echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo "1. Start the backend: cd rag_backend && source venv/bin/activate && python main.py"
echo "2. Start the frontend: cd rag_frontend && npm start"
echo ""
echo "The application will be available at: http://localhost:3000"
