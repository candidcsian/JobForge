#!/bin/bash

# JobForge Demo Script

echo "🔨 JobForge Demo"
echo "================"
echo ""

cd ~/JobForge

echo "1️⃣  Testing Match Command..."
python3 jobforge.py match
echo ""

echo "2️⃣  Showing Top Matches..."
python3 jobforge.py show --top 5
echo ""

echo "3️⃣  Generating Resumes..."
python3 jobforge.py forge --top 2 --min-score 50
echo ""

echo "4️⃣  Exporting Results..."
python3 jobforge.py export --output demo-results.csv
echo ""

echo "✅ Demo Complete!"
echo ""
echo "📂 Check these files:"
echo "   - results/matches/*/scored_jobs.csv"
echo "   - results/resumes/*.md"
echo "   - demo-results.csv"
