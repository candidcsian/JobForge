#!/bin/bash
# JobBell - One-Command Installer & Runner
# This script downloads itself and runs locally to preserve stdin

SCRIPT_URL="https://raw.githubusercontent.com/candidcsian/JobBell/main/jobbell_run.sh"
LOCAL_SCRIPT="/tmp/jobbell_run_$$.sh"

# Download the actual script
curl -sSL "$SCRIPT_URL" -o "$LOCAL_SCRIPT"

# Make it executable
chmod +x "$LOCAL_SCRIPT"

# Run it (this preserves stdin for interactive input)
bash "$LOCAL_SCRIPT"

# Cleanup
rm -f "$LOCAL_SCRIPT"
