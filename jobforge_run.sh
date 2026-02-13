#!/bin/bash
# JobForge - Installer Script

set -e

echo "🚀 JobForge - AI-Powered Career Assistant"
echo "=========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi

# Setup directory
JOBFORGE_DIR="$HOME/JobForge"

if [ ! -d "$JOBFORGE_DIR" ]; then
    echo "📥 Installing JobForge..."
    git clone -q https://github.com/candidcsian/JobForge.git "$JOBFORGE_DIR" 2>/dev/null || {
        echo "❌ Git not found. Installing..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            xcode-select --install
        fi
        git clone -q https://github.com/candidcsian/JobForge.git "$JOBFORGE_DIR"
    }
else
    echo "📥 Updating JobForge..."
    cd "$JOBFORGE_DIR"
    git pull -q 2>/dev/null || true
fi

cd "$JOBFORGE_DIR"

# Setup venv
if [ ! -d "venv" ]; then
    echo "🔧 Setting up environment..."
    python3 -m venv venv
fi

# Activate and install
source venv/bin/activate
pip install -q --upgrade pip python-docx pyyaml httpx 2>/dev/null

echo ""
echo "✅ Installation Complete!"
echo ""
echo "========================================================================"
echo "To start JobForge, run:"
echo "  cd ~/JobForge && ./start_agent.sh"
echo "========================================================================"
echo ""
