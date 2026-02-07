#!/bin/bash
# JobForge - Publish to GitHub Script

echo "🚀 JobForge - Publishing to GitHub"
echo "=================================="
echo ""

# Step 1: Check for sensitive files
echo "📋 Step 1: Checking for sensitive files..."
if git status | grep -q "senthil-master.md\|Senthil_Kumar_ATS_Resume\|LinkedIn_Profile.md"; then
    echo "⚠️  WARNING: Sensitive files detected!"
    echo "Please review .gitignore and remove sensitive files."
    exit 1
fi
echo "✅ No sensitive files detected"
echo ""

# Step 2: Copy GitHub README
echo "📄 Step 2: Preparing README..."
cp README_GITHUB.md README.md
echo "✅ README prepared"
echo ""

# Step 3: Add files
echo "📦 Step 3: Adding files to git..."
git add .
echo "✅ Files added"
echo ""

# Step 4: Show status
echo "📊 Step 4: Files to be committed:"
git status --short
echo ""

# Step 5: Confirm
read -p "Do these files look correct? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "❌ Aborted. Please review files and try again."
    exit 1
fi
echo ""

# Step 6: Commit
echo "💾 Step 5: Committing..."
git commit -m "Initial commit: JobForge - AI-Powered Career Assistant

Features:
- Interactive agent for resume building
- ATS-optimized resume generation
- LinkedIn profile optimization
- Job portal setup guides
- Job search strategy

All user data stays private (excluded from git)"
echo "✅ Committed"
echo ""

# Step 7: Instructions for GitHub
echo "🌐 Step 6: Create GitHub Repository"
echo "=================================="
echo ""
echo "1. Go to: https://github.com/new"
echo "2. Repository name: JobForge"
echo "3. Description: AI-Powered Career Assistant - Build Your Perfect Resume in 2 Hours"
echo "4. Visibility: Public (or Private)"
echo "5. DO NOT initialize with README"
echo "6. Click 'Create repository'"
echo ""
read -p "Press Enter when you've created the repository..."
echo ""

# Step 8: Get GitHub username
read -p "Enter your GitHub username: " github_user
echo ""

# Step 9: Add remote and push
echo "🚀 Step 7: Pushing to GitHub..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/$github_user/JobForge.git
git branch -M main

echo ""
echo "Pushing to GitHub..."
if git push -u origin main; then
    echo ""
    echo "🎉 SUCCESS! JobForge is now on GitHub!"
    echo "=================================="
    echo ""
    echo "📍 Your repository: https://github.com/$github_user/JobForge"
    echo ""
    echo "🤝 Share with friends:"
    echo "   git clone https://github.com/$github_user/JobForge.git"
    echo "   cd JobForge"
    echo "   ./start_agent.sh"
    echo ""
    echo "⭐ Don't forget to star your own repo!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo "   1. Check your GitHub credentials"
    echo "   2. Make sure repository was created"
    echo "   3. Try: git push -u origin main --force"
    echo ""
fi
