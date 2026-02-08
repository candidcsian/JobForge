# JobBell - Usage Guide

## 🎯 Two Ways to Use JobBell

### 1. Interactive Mode (Easiest)

```bash
cd ~/JobBell
python3 interactive.py
```

**What happens:**
1. ✅ Asks for your resume (upload PDF/DOCX or enter manually)
2. ✅ Asks for recent achievements
3. ✅ Asks for job preferences (titles, locations)
4. ✅ Asks if you want remote-only jobs
5. ✅ Runs discovery, matching, and resume generation
6. ✅ Shows results

**Example session:**
```
🔨 Welcome to JobBell - Interactive Setup
==================================================

📄 Step 1: Resume
How would you like to provide your experience?
  1. Upload resume (PDF/DOCX)
  2. Enter career history manually
  3. Use existing career/ files

Choice (1-3): 1
Enter resume path: ~/Downloads/my-resume.pdf
✅ Will parse: ~/Downloads/my-resume.pdf

🏆 Step 2: Recent Achievements (Optional)
Achievement (or Enter to continue): Led team of 5 engineers
Achievement (or Enter to continue): Reduced latency by 60%
Achievement (or Enter to continue): 
✅ Added 2 achievements

🎯 Step 3: Job Preferences
Target job titles (comma-separated): Machine Learning Engineer, Senior Software Engineer
Preferred locations (comma-separated, or 'remote'): Remote, California

🔍 Step 4: Search Options
What would you like to do?
  1. Search all companies
  2. Search specific companies
  3. Search only remote jobs

Choice (1-3): 3
✅ Will search remote jobs only

⚡ Running JobBell...
[Results shown here]
```

### 2. Command Line Mode (Advanced)

```bash
cd ~/JobBell

# Step-by-step
python3 jobbell.py discover
python3 jobbell.py match --resume ~/Downloads/resume.pdf
python3 jobbell.py show --top 20
python3 jobbell.py forge --top 10
```

## 🌍 Remote Jobs Only

### Option 1: In Interactive Mode
```bash
python3 interactive.py
# Choose option 3: "Search only remote jobs"
```

### Option 2: In settings.yaml
```yaml
locations:
  - Remote
```

### Option 3: Filter after matching
```bash
python3 jobbell.py match
python3 jobbell.py show --top 50 | grep -i remote
```

## 📤 Sharing JobBell

### Publish to GitHub

```bash
cd ~/JobBell

# Step 1: Commit your code
git add .
git commit -m "Initial commit"

# Step 2: Run publish script
./publish.sh

# Follow the instructions to:
# 1. Create GitHub repo
# 2. Push code
# 3. Share link
```

### Share with Someone

**Option 1: GitHub (Public)**
```bash
./publish.sh
# Share: https://github.com/YOUR_USERNAME/JobBell
```

**Option 2: GitHub (Private)**
```bash
# After publishing as private
# Add collaborators: Settings → Collaborators → Add people
```

**Option 3: Zip File**
```bash
cd ~
tar -czf JobBell.tar.gz JobBell/
# Send JobBell.tar.gz via email/drive
```

**Option 4: Direct Clone (if on same network)**
```bash
# On your machine
cd ~/JobBell
python3 -m http.server 8000

# On their machine
wget http://YOUR_IP:8000/JobBell.tar.gz
tar -xzf JobBell.tar.gz
```

## 📋 Complete Workflow Examples

### Example 1: First Time User (Interactive)

```bash
cd ~/JobBell
python3 interactive.py

# Follow prompts:
# - Upload resume: ~/Documents/resume.pdf
# - Achievements: "Launched 3 major features"
# - Titles: "Software Engineer, ML Engineer"
# - Locations: "Remote"
# - Search: Remote jobs only
# - Generate: Top 10 resumes

# Results in:
# - results/matches/scored_jobs.csv
# - results/resumes/*.md
```

### Example 2: Weekly Job Search (CLI)

```bash
cd ~/JobBell

# Monday: Find new jobs
python3 jobbell.py discover

# Tuesday: Match and review
python3 jobbell.py match --min-score 70
python3 jobbell.py show --top 20

# Wednesday: Generate resumes
python3 jobbell.py forge --top 10

# Thursday: Export for tracking
python3 jobbell.py export --output weekly-jobs.csv
```

### Example 3: Remote Jobs Only

```bash
# Edit settings
vim config/settings.yaml
# Set: locations: [Remote]

# Run matching
python3 jobbell.py match

# View remote jobs
python3 jobbell.py show --top 50
```

### Example 4: Specific Companies

```bash
python3 jobbell.py discover --companies "OpenAI,Anthropic,Google"
python3 jobbell.py match
python3 jobbell.py show --company "OpenAI"
```

## 🔧 Configuration Files

### For Remote Jobs: config/settings.yaml
```yaml
job_titles:
  - Software Engineer
  - Machine Learning Engineer

locations:
  - Remote          # Only remote jobs
  # - California    # Or specific locations
  # - New York

exclude_levels:
  - junior
  - intern

min_match_score: 60
```

### For Specific Companies: config/companies.yaml
```yaml
companies:
  - name: OpenAI
    career_url: https://jobs.ashbyhq.com/openai
    ats_type: ashby
  
  # Add more companies here
```

## 📊 Understanding Results

### scored_jobs.csv
```csv
Score,Company,Title,Location,URL
95,OpenAI,ML Engineer,Remote,https://...
87,Anthropic,Research Scientist,San Francisco / Remote,https://...
78,Google,Senior SWE,Remote,https://...
```

**Score breakdown:**
- 80-100%: ⭐⭐⭐ Strong match - Apply immediately
- 60-79%: ⭐⭐ Good match - Consider applying
- 40-59%: ⭐ Partial match - Review carefully

**Remote indicator:**
- Jobs with "Remote" in location are flagged
- Get +5 bonus points in scoring

## 🚀 Publishing to GitHub

### Step-by-Step

1. **Create GitHub Account** (if needed)
   - Go to https://github.com/signup

2. **Run Publish Script**
   ```bash
   cd ~/JobBell
   ./publish.sh
   ```

3. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Name: `JobBell`
   - Description: `AI-powered job search automation`
   - Public or Private: Your choice
   - **Don't** initialize with README

4. **Push Code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/JobBell.git
   git branch -M main
   git push -u origin main
   ```

5. **Share Link**
   ```
   https://github.com/YOUR_USERNAME/JobBell
   ```

### Making it Public

Anyone can then use it:
```bash
git clone https://github.com/YOUR_USERNAME/JobBell.git
cd JobBell
./setup.sh
python3 interactive.py
```

## 💡 Tips

1. **Update career/ monthly** - Keep profile current
2. **Run weekly** - Catch new postings early
3. **Use interactive mode** - Easier for first time
4. **Filter for remote** - Set in settings.yaml
5. **Track applications** - Use exported CSV
6. **Share on GitHub** - Help others find jobs too!

## ❓ FAQ

**Q: How do I search only remote jobs?**
A: Set `locations: [Remote]` in config/settings.yaml or use interactive mode option 3

**Q: Can I upload my resume?**
A: Yes! Use `python3 interactive.py` or `python3 jobbell.py match --resume path/to/resume.pdf`

**Q: How do I share this with friends?**
A: Run `./publish.sh` and push to GitHub, then share the link

**Q: Is my data private?**
A: Yes! Everything runs locally. Only you see your data unless you push to public GitHub

**Q: Can I search specific companies?**
A: Yes! `python3 jobbell.py discover --companies "OpenAI,Google"`

---

**Ready to forge your career path!** 🔨
