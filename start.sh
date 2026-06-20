#!/bin/bash

# Quick Start Script for Voice Teaching Assistant
# Run this after initial setup

echo "🚀 Starting Voice Teaching Assistant..."
echo ""

# Check if backend/.env exists
if [ ! -f "backend/.env" ]; then
    echo "❌ Error: backend/.env file not found!"
    echo "   Please create it from backend/.env.example and add your GEMINI_API_KEY"
    exit 1
fi

# Start backend
echo "📦 Starting backend server..."
cd backend
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null || {
    echo "❌ Virtual environment not found. Run setup first:"
    echo "   cd backend && python -m venv venv && pip install -r requirements.txt"
    exit 1
}

python app.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
sleep 3

# Start frontend
echo "🎨 Starting frontend..."
cd frontend

if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Application started!"
echo ""
echo "Backend:  http://localhost:5000"
echo "Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for Ctrl+C
trap "echo ''; echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait
