# 🚀 Get Started with JobBell

## What You Have Now

A complete job search automation tool in `~/JobBell/` with:

✅ **CLI Framework** - All commands working
✅ **Matching Engine** - Scores jobs against your profile  
✅ **Resume Templates** - Ready for AI generation
✅ **Example Data** - Test with sample career history
✅ **Documentation** - Complete guides

## Try It Right Now (2 minutes)

\`\`\`bash
cd ~/JobBell

# Test matching with example data
python3 jobbell.py match

# View help
python3 jobbell.py --help

# See all commands
python3 jobbell.py discover --help
python3 jobbell.py match --help
python3 jobbell.py forge --help
\`\`\`

## Set Up For Real Use (10 minutes)

### 1. Add Your Career History

\`\`\`bash
# Edit the example files
vim career/2024.md
vim career/2023.md

# Or create new ones
vim career/2025.md
\`\`\`

Add your real experience:
\`\`\`markdown
# 2024 Work Experience

## Your Title at Your Company (Start - End)

### Responsibilities
- What you did
- Technologies you used

### Skills
Python, AWS, Docker, Kubernetes, etc.
\`\`\`

### 2. Configure Preferences

\`\`\`bash
vim config/settings.yaml
\`\`\`

Set your target roles and locations:
\`\`\`yaml
job_titles:
  - Your Target Role
  - Another Role

locations:
  - Your City
  - Remote
\`\`\`

### 3. Test Matching

\`\`\`bash
python3 jobbell.py match
\`\`\`

You should see your skills extracted from career files.

## Add Job Discovery (Next Step)

JobBell matching works now. To add job discovery:

### Option 1: Use Argus Separately (Quick)

\`\`\`bash
# In another terminal
cd ~/Argus
python run_search.py

# Copy results to JobBell
cp -r job_results/default/* ~/JobBell/results/jobs/

# Back to JobBell
cd ~/JobBell
python3 jobbell.py match
\`\`\`

### Option 2: Integrate Argus (Better)

\`\`\`bash
# Copy Argus modules
cp -r ~/Argus/Argus/* ~/JobBell/core/discovery/

# Update imports in core/discovery/orchestrator.py
# Then run
python3 jobbell.py discover
\`\`\`

## Full Workflow

Once discovery is integrated:

\`\`\`bash
# Weekly routine
python3 jobbell.py discover              # Find jobs
python3 jobbell.py match --min-score 70  # Score them
python3 jobbell.py show --top 20         # View top matches
python3 jobbell.py forge --top 10        # Generate resumes
python3 jobbell.py export --output jobs.csv  # Export for tracking
\`\`\`

## What Each File Does

\`\`\`
JobBell/
├── README.md           # Main documentation
├── QUICKSTART.md       # Quick start guide
├── WORKFLOW.md         # Visual workflow explanation
├── ARCHITECTURE.md     # Technical details
├── GET_STARTED.md      # This file
│
├── jobbell.py         # Main CLI (run this)
├── setup.sh            # Setup script
│
├── core/
│   ├── discovery/      # Job crawling (integrate Argus here)
│   ├── matching/       # Scoring engine (WORKING NOW)
│   ├── forge/          # Resume generation (templates ready)
│   └── cli/            # Display, export utilities
│
├── career/             # YOUR EXPERIENCE (edit these)
│   ├── 2024.md
│   └── 2023.md
│
├── config/             # YOUR PREFERENCES (edit these)
│   ├── settings.yaml
│   └── companies.yaml
│
└── results/            # OUTPUT (generated)
    ├── jobs/           # Discovered jobs
    ├── matches/        # Scored matches
    └── resumes/        # Generated resumes
\`\`\`

## Commands Reference

\`\`\`bash
# Discovery
jobbell discover                    # Find all jobs
jobbell discover --companies "OpenAI,Google"  # Specific companies

# Matching
jobbell match                       # Score all jobs
jobbell match --min-score 70        # Only 70%+ matches
jobbell match --resume resume.pdf   # Use PDF instead of career/

# Resume Generation
jobbell forge --top 10              # Generate for top 10
jobbell forge --min-score 80        # Only 80%+ matches

# Viewing Results
jobbell show --top 20               # Show top 20
jobbell show --company "OpenAI"     # Filter by company
jobbell export --output jobs.csv    # Export to CSV

# Setup
jobbell init --example              # Initialize new project
\`\`\`

## Tips

1. **Update career/ monthly** - Keep your profile current
2. **Run discovery weekly** - Catch new postings early
3. **Set min-score 70+** - Focus on quality matches
4. **Review generated resumes** - Always customize before sending
5. **Track applications** - Use exported CSV

## Troubleshooting

**"No jobs to match"**
→ Run discovery first or copy jobs from Argus

**"Career directory not found"**
→ Make sure you're in ~/JobBell directory

**Low match scores**
→ Add more skills and technologies to career/*.md

## Next Steps

1. ✅ Test matching with example data
2. ✏️ Add your real career history
3. 🔍 Integrate job discovery
4. 🎯 Run full workflow
5. 📝 Apply to top matches!

## Questions?

- Read: README.md (full docs)
- Read: WORKFLOW.md (visual guide)
- Read: ARCHITECTURE.md (technical details)

---

**You're ready to forge your career path!** 🔨
