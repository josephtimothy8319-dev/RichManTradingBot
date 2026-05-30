#!/bin/bash

# RichManBot - Run Script

echo "🚀 Starting RichManBot..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run the server
echo ""
echo "✅ Starting FastAPI server..."
echo "📊 Dashboard available at: http://localhost:8000/static/index.html"
echo ""

python backend/main.py
