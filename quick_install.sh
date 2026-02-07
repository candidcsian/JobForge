#!/bin/bash
# JobForge - Quick Installer (Downloads then runs locally)

set -e

echo "🚀 JobForge - AI-Powered Career Assistant"
echo "=========================================="
echo ""

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    *)          MACHINE="UNKNOWN:${OS}"
esac

echo "📍 Detected: $MACHINE"
echo ""

# Check Python
echo "🔍 Checking Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
    echo "✅ Python $PYTHON_VERSION found"
else
    echo "❌ Python 3 not found!"
    echo ""
    echo "Please install Python 3.9 or higher:"
    if [ "$MACHINE" = "Mac" ]; then
        echo "  brew install python3"
    elif [ "$MACHINE" = "Linux" ]; then
        echo "  sudo apt-get install python3 python3-pip"
    fi
    exit 1
fi
echo ""

# Check if already installed
if [ -d "$HOME/JobForge" ]; then
    echo "📂 JobForge found at ~/JobForge"
    echo ""
    read -p "Update to latest version? (y/n): " UPDATE
    if [ "$UPDATE" = "y" ] || [ "$UPDATE" = "Y" ]; then
        echo "🔄 Updating..."
        cd "$HOME/JobForge"
        git pull
        echo "✅ Updated!"
    fi
else
    # Clone repository
    echo "📥 Downloading JobForge..."
    cd "$HOME"
    git clone https://github.com/candidcsian/JobForge.git
    echo "✅ Downloaded!"
fi
echo ""

# Go to JobForge directory
cd "$HOME/JobForge"

# Create virtual environment
echo "🔧 Setting up environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet python-docx pyyaml

echo "✅ Setup complete!"
echo ""
echo "="*70
echo "🎯 JobForge is ready!"
echo "="*70
echo ""
echo "To start building your resume, run:"
echo ""
echo "  cd ~/JobForge"
echo "  ./start_agent.sh"
echo ""
echo "Or for a quick test:"
echo ""
echo "  cd ~/JobForge"
echo "  python3 test_agent.py"
echo ""
