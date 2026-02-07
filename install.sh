#!/bin/bash
# JobForge - One-Command Installer & Runner
# Usage: curl -sSL https://raw.githubusercontent.com/candidcsian/JobForge/main/install.sh | bash

set -e

echo "🚀 JobForge - AI-Powered Career Assistant"
echo "=========================================="
echo ""

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    CYGWIN*)    MACHINE=Windows;;
    MINGW*)     MACHINE=Windows;;
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
    echo "📂 JobForge already installed at ~/JobForge"
    echo ""
    read -p "Do you want to update it? (y/n): " UPDATE
    if [ "$UPDATE" = "y" ] || [ "$UPDATE" = "Y" ]; then
        echo "🔄 Updating JobForge..."
        cd "$HOME/JobForge"
        git pull
        echo "✅ Updated!"
    fi
else
    # Clone repository
    echo "📥 Downloading JobForge..."
    cd "$HOME"
    if command -v git &> /dev/null; then
        git clone https://github.com/candidcsian/JobForge.git
    else
        echo "❌ Git not found. Installing..."
        if [ "$MACHINE" = "Mac" ]; then
            xcode-select --install
        elif [ "$MACHINE" = "Linux" ]; then
            sudo apt-get install -y git
        fi
        git clone https://github.com/candidcsian/JobForge.git
    fi
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

# Run the agent
echo "🎯 Starting JobForge Agent..."
echo ""
python3 test_agent.py

echo ""
echo "✅ JobForge test complete!"
echo ""
echo "📂 Your files are in: ~/JobForge"
echo "   - Career profile: ~/JobForge/career/"
echo "   - Resume: ~/JobForge/results/resumes/"
echo ""
echo "🔄 To run again: cd ~/JobForge && ./start_agent.sh"
echo ""
