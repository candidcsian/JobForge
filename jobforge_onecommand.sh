#!/bin/bash
# JobForge - One-Command Installer
# Downloads and installs JobForge

SCRIPT_URL="https://raw.githubusercontent.com/candidcsian/JobForge/main/jobforge_run.sh"
LOCAL_SCRIPT="/tmp/jobforge_install_$$.sh"

# Download the installer
curl -sSL "$SCRIPT_URL" -o "$LOCAL_SCRIPT"

# Make it executable
chmod +x "$LOCAL_SCRIPT"

# Run installer
bash "$LOCAL_SCRIPT"

# Cleanup
rm -f "$LOCAL_SCRIPT"
