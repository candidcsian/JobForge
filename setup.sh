#!/bin/bash

# JobForge Setup Script

echo "🔨 JobForge Setup"
echo "================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Install Playwright
echo ""
echo "🎭 Installing Playwright browsers..."
python3 -m playwright install chromium

# Make jobforge executable
chmod +x jobforge.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Activate environment: source venv/bin/activate"
echo "  2. Edit career/*.md with your experience"
echo "  3. Run: python3 jobforge.py discover"
echo ""
echo "Optional: Install Bun for AI resume generation"
echo "  curl -fsSL https://bun.sh/install | bash"
