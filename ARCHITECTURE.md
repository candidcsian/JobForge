# JobBell - Complete Job Search Automation

## 🎯 What is JobBell?

**JobBell** is an AI-powered job search automation tool that:
1. **Discovers** jobs from 50+ tech companies automatically
2. **Matches** jobs to your background with intelligent scoring
3. **Forges** tailored resumes for each application using AI

## 🏗️ Architecture

JobBell combines three powerful open-source projects:

1. **Argus** (Job Discovery) - Crawls career pages across multiple ATS platforms
2. **Resume Parser** (Matching) - Extracts skills and scores job relevance
3. **Resume Context Builder** (Generation) - Creates tailored resumes with LLM

## 📁 Project Structure

```
JobBell/
├── jobbell.py              # Main CLI entry point
├── core/
│   ├── discovery/           # Job crawling engine
│   ├── matching/            # Resume parsing & scoring
│   ├── forge/               # Resume generation
│   └── cli/                 # CLI utilities
├── career/                  # Your career history (markdown)
├── config/
│   ├── companies.yaml       # Companies to search
│   └── settings.yaml        # Your preferences
├── results/
│   ├── jobs/               # Discovered jobs
│   ├── matches/            # Scored matches
│   └── resumes/            # Generated resumes
└── templates/              # Resume templates
```

## 🚀 Commands

### Discovery
```bash
python3 jobbell.py discover [--companies "OpenAI,Google"] [--timeout 60]
```
Crawls company career pages and saves jobs to `results/jobs/`

### Matching
```bash
python3 jobbell.py match [--min-score 60] [--career-dir career]
```
Scores jobs against your profile, saves to `results/matches/`

### Forge
```bash
python3 jobbell.py forge --top 10 [--min-score 70] [--type software-engineer]
```
Generates tailored resumes for top matches

### Show
```bash
python3 jobbell.py show --top 20 [--company "OpenAI"] [--min-score 70]
```
Display match results in terminal

### Export
```bash
python3 jobbell.py export --output jobs.csv [--min-score 60]
```
Export results to CSV

### Init
```bash
python3 jobbell.py init [--example]
```
Initialize JobBell in current directory

## 🎨 Features

### Job Discovery
- ✅ Multi-ATS support (Greenhouse, Lever, Ashby, Workday, etc.)
- ✅ 50+ pre-configured tech companies
- ✅ Auto-detection of job board types
- ✅ Incremental updates (no duplicates)
- ✅ Configurable timeout and retries

### Intelligent Matching
- ✅ Parses career history from markdown
- ✅ Extracts skills, titles, experience
- ✅ Scores jobs 0-100% based on:
  - Title match (40%)
  - Skills match (40%)
  - Experience level (20%)
- ✅ Detailed match reports
- ✅ CSV export for tracking

### Resume Generation
- ✅ AI-powered tailoring (uses your LLM)
- ✅ Job-specific customization
- ✅ ATS-optimized format
- ✅ Batch generation for top matches
- ✅ Markdown output (PDF-ready)

## 📊 Workflow

```
Week 1: Setup
├── Add career history to career/*.md
├── Configure preferences in config/settings.yaml
└── Run initial discovery

Week 2+: Weekly Routine
├── python3 jobbell.py discover        # Find new jobs
├── python3 jobbell.py match           # Score against profile
├── python3 jobbell.py show --top 20   # Review top matches
├── python3 jobbell.py forge --top 10  # Generate resumes
└── Apply to top matches with tailored resumes
```

## 🔧 Configuration

### Career History (career/*.md)
```markdown
# 2024 Work Experience

## Senior Engineer at TechCorp (2024 - Present)
- Built ML pipeline with Python and TensorFlow
- Deployed on AWS with Docker and Kubernetes
**Skills**: Python, TensorFlow, AWS, Docker, Kubernetes
```

### Settings (config/settings.yaml)
```yaml
job_titles:
  - Machine Learning Engineer
  - Senior Software Engineer

locations:
  - California
  - Remote

exclude_levels:
  - junior
  - intern

min_match_score: 60
```

### Companies (config/companies.yaml)
```yaml
companies:
  - name: OpenAI
    career_url: https://jobs.ashbyhq.com/openai
    ats_type: ashby
```

## 📈 Example Output

```
🎯 JobBell - Job Matching
==================================================

📊 Profile Summary:
   Skills: 21 identified
   Titles: 2 identified
   Experience: ~5 years

🔍 Found 287 jobs to analyze

✨ Found 95 matching jobs

🏆 Top 10 Matches:
======================================================================

1. OpenAI - Machine Learning Engineer
   Score: 95% ⭐⭐⭐
   https://jobs.ashbyhq.com/openai/ml-engineer

2. Anthropic - Research Scientist
   Score: 87% ⭐⭐⭐
   https://boards.greenhouse.io/anthropic/scientist

3. Google - Senior Software Engineer
   Score: 78% ⭐⭐
   https://careers.google.com/jobs/senior-swe
```

## 🛠️ Development Status

### ✅ Completed
- Core CLI framework
- Career history parsing
- Job matching algorithm
- Resume generation templates
- Result display and export
- Configuration system

### 🚧 In Progress
- Integration with Argus discovery engine
- LLM integration for resume generation
- Enhanced scoring algorithm
- PDF export for resumes

### 📋 Planned
- Web UI dashboard
- Application tracking
- Email notifications for new matches
- LinkedIn integration
- Cover letter generation
- Interview preparation suggestions

## 🤝 Contributing

We welcome contributions! Areas to help:

1. **ATS Adapters** - Add support for more job boards
2. **Resume Templates** - Share effective formats
3. **Company Configs** - Add more companies
4. **LLM Providers** - Integrate additional AI services
5. **Documentation** - Improve guides and examples

## 📄 License

MIT License - Free and open source

## 🙏 Credits

Built by combining:
- [Argus](https://github.com/mshen1019/Argus) by mshen1019
- [Resume Context Builder](https://github.com/tituslesley89/resume-context-builder) by tituslesley89

## 📞 Support

- GitHub Issues: Report bugs and request features
- Discussions: Ask questions and share tips
- Documentation: Full guides in `/docs`

---

**JobBell - Forge your career path with AI** 🔨

*Made with AI, for humans looking for their next opportunity.*
