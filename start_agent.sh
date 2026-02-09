#!/bin/bash
# JobForge Agent Launcher

echo "🔔 Starting JobForge Agent..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python3 -c "import docx" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install python-docx pyyaml httpx -q
fi

# Run the agent
python3 jobforge_agent.py

echo ""
echo "✅ JobForge Agent completed!"
