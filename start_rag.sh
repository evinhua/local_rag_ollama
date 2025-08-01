#!/bin/bash

echo "🚀 Starting Local RAG Solution..."

# Function to cleanup background processes
cleanup() {
    echo "🛑 Shutting down..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
    fi
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "⚠️  Ollama is not running. Please start Ollama first."
    echo "   Run: ollama serve"
    exit 1
fi

# Kill any existing processes on the ports
echo "🧹 Cleaning up existing processes..."
lsof -ti:8000 | xargs kill -9 2>/dev/null || true
lsof -ti:3000 | xargs kill -9 2>/dev/null || true

# Start backend
echo "🐍 Starting Python backend..."
cd rag_backend
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
for i in {1..30}; do
    if curl -s http://localhost:8000/health > /dev/null; then
        echo "✅ Backend is ready!"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "❌ Backend failed to start"
        kill $BACKEND_PID 2>/dev/null
        exit 1
    fi
    sleep 1
done

# Start frontend
echo "⚛️  Starting React frontend..."
cd ../rag_frontend
npm start &
FRONTEND_PID=$!

echo "✅ Both services started!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo "🤖 Using models: BGE-M3 (embeddings) + Gemma3:4b (generation)"
echo ""
echo "Press Ctrl+C to stop both services"

# Wait for processes
wait
