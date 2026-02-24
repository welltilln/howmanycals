#!/bin/bash

echo "========================================="
echo "🍲 How Many Cals Bot Setup"
echo "========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Error: python3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️ .env file not found! Copying from .env.example..."
    cp .env.example .env
    echo "👉 Please open the .env file and add your GEMINI and LINE API keys, then run this script again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing requirements (this might take a moment)..."
pip install -r requirements.txt --quiet

# Run the app
echo "🚀 Starting the connector..."
python main.py
