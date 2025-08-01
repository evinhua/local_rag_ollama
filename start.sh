#!/bin/bash

echo "🚀 Starting Local RAG Solution..."

# Function to cleanup background processes
cleanup() {
    echo "🛑 Shutting down..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Start backend
echo "🐍 Starting Python backend..."
cd rag_backend
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "⚛️  Starting React frontend..."
cd ../rag_frontend
npm start &
FRONTEND_PID=$!

echo "✅ Both services started!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both services"

# Wait for processes
wait
