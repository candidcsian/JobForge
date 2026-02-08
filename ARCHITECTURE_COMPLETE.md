# 🏗️ JobBell - Complete Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         JobBell                                 │
│         AI-Powered Job Search + Referral System                 │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   DISCOVER   │───▶│    MATCH     │───▶│   REFERRAL   │───▶│    FORGE     │
│              │    │              │    │              │    │              │
│ Crawl 53     │    │ Score jobs   │    │ Find         │    │ Generate     │
│ companies    │    │ 0-100%       │    │ employees    │    │ tailored     │
│              │    │              │    │              │    │ resumes      │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
      │                    │                    │                    │
      ▼                    ▼                    ▼                    ▼
  287 jobs            95 matches         LinkedIn links        10 resumes
```

## Directory Structure

```
JobBell/
├── jobbell.py                 # Main CLI entry point
├── interactive.py              # Interactive wizard
│
├── core/                       # Core modules
│   ├── discovery/              # Job discovery engine
│   │   ├── orchestrator.py    # Coordinates crawling
│   │   ├── models.py           # Job/Company models
│   │   ├── store.py            # Save jobs to disk
│   │   ├── filter.py           # Filter by location/title
│   │   └── ats/                # ATS adapters
│   │       ├── greenhouse.py  # Greenhouse crawler
│   │       ├── lever.py        # Lever crawler
│   │       ├── ashby.py        # Ashby crawler
│   │       ├── workday.py      # Workday crawler
│   │       ├── amazon.py       # Amazon crawler
│   │       ├── google.py       # Google crawler
│   │       ├── meta.py         # Meta crawler
│   │       └── generic.py      # Fallback crawler
│   │
│   ├── matching/               # Job matching engine
│   │   ├── matcher.py          # Main matching logic
│   │   ├── parser.py           # Resume parser (PDF/DOCX)
│   │   └── scorer.py           # Scoring algorithm
│   │
│   ├── referral/               # Referral system (NEW!)
│   │   ├── finder.py           # Find employees
│   │   └── messages.py         # Message templates
│   │
│   ├── forge/                  # Resume generation
│   │   ├── generator.py        # Main generator
│   │   └── resume_templates.py # Amazon-style templates
│   │
│   └── cli/                    # CLI utilities
│       ├── display.py          # Show results
│       ├── export.py           # Export to CSV
│       └── init.py             # Initialize project
│
├── career/                     # User's career history
│   ├── 2024.md                # Current experience
│   └── 2023.md                # Previous experience
│
├── config/                     # Configuration
│   ├── companies.yaml         # 53 companies to search
│   └── settings.yaml          # User preferences
│
├── results/                    # Output
│   ├── jobs/                  # Discovered jobs
│   │   └── 2026-02-01/
│   │       └── [company]/
│   │           └── jobs.json
│   │
│   ├── matches/               # Scored matches
│   │   └── 2026-02-01/
│   │       ├── scored_jobs.json
│   │       ├── scored_jobs.csv
│   │       └── employee_search.json  # NEW!
│   │
│   └── resumes/               # Generated resumes
│       ├── openai-ml-engineer.md
│       └── anthropic-swe.md
│
└── docs/                       # Documentation
    ├── README.md
    ├── QUICKSTART.md
    ├── WORKFLOW.md
    ├── REFERRAL_GUIDE.md      # NEW!
    └── ADD_COMPANIES.md
```

## Data Flow

### 1. Discovery Phase

```
User runs: python3 jobbell.py discover

orchestrator.py
    │
    ├─▶ Load config/companies.yaml (53 companies)
    │
    ├─▶ For each company:
    │   │
    │   ├─▶ Select ATS adapter (greenhouse/lever/ashby/etc)
    │   │
    │   ├─▶ Fetch jobs from career page
    │   │   └─▶ HTTP request → Parse HTML/JSON → Extract jobs
    │   │
    │   └─▶ Save to results/jobs/[date]/[company]/jobs.json
    │
    └─▶ Output: 287 jobs found across 53 companies
```

### 2. Matching Phase

```
User runs: python3 jobbell.py match

matcher.py
    │
    ├─▶ Load career/*.md files
    │   └─▶ Extract: skills, titles, years of experience
    │
    ├─▶ Load all jobs from results/jobs/
    │
    ├─▶ For each job:
    │   │
    │   ├─▶ Calculate score (0-100%):
    │   │   ├─▶ Title match: 40 points
    │   │   ├─▶ Skills match: 40 points
    │   │   └─▶ Experience match: 20 points
    │   │
    │   └─▶ Filter by min_score (default: 60%)
    │
    ├─▶ Sort by score (highest first)
    │
    └─▶ Save to results/matches/[date]/scored_jobs.json
        Output: 95 matching jobs (60%+)
```

### 3. Referral Phase (NEW!)

```
User runs: python3 jobbell.py referral --top 10

finder.py
    │
    ├─▶ Load results/matches/[date]/scored_jobs.json
    │
    ├─▶ Get top 10 jobs
    │
    ├─▶ Group by company
    │
    ├─▶ For each company:
    │   │
    │   ├─▶ Generate LinkedIn search URLs:
    │   │   ├─▶ All employees
    │   │   ├─▶ Engineers
    │   │   └─▶ Recruiters
    │   │
    │   └─▶ Show open roles at that company
    │
    └─▶ Save to results/matches/[date]/employee_search.json
        Output: LinkedIn links for 10 companies
```

### 4. Forge Phase

```
User runs: python3 jobbell.py forge --top 10

generator.py
    │
    ├─▶ Load results/matches/[date]/scored_jobs.json
    │
    ├─▶ Get top 10 jobs
    │
    ├─▶ For each job:
    │   │
    │   ├─▶ Load career/*.md files
    │   │
    │   ├─▶ Generate resume using Amazon patterns:
    │   │   ├─▶ Summary (impact-focused)
    │   │   ├─▶ Experience (quantified achievements)
    │   │   ├─▶ Skills (categorized)
    │   │   └─▶ "Why [Company]" section
    │   │
    │   └─▶ Save to results/resumes/[company]-[title].md
    │
    └─▶ Output: 10 tailored resumes
```

## Key Components

### 1. Discovery Engine

**Purpose**: Crawl 53 company career pages and extract job listings

**Components**:
- `orchestrator.py` - Coordinates the crawling process
- `ats/` - ATS-specific adapters (Greenhouse, Lever, etc.)
- `store.py` - Saves jobs to JSON files

**Supported ATS**:
- Greenhouse (most startups)
- Lever (Spotify, Palantir)
- Ashby (OpenAI, Scale AI)
- Workday (Microsoft, Apple)
- Custom (Amazon, Google, Meta)

### 2. Matching Engine

**Purpose**: Score jobs against user's profile

**Algorithm**:
```python
score = title_match(40) + skills_match(40) + experience_match(20)

if score >= min_score:
    matched_jobs.append(job)
```

**Inputs**:
- Career history (career/*.md)
- Job listings (results/jobs/)

**Outputs**:
- Scored jobs (results/matches/scored_jobs.json)
- CSV for tracking (results/matches/scored_jobs.csv)

### 3. Referral System (NEW!)

**Purpose**: Help users get referrals instead of cold applying

**Features**:
- Generate LinkedIn search URLs
- Find employees at target companies
- Provide message templates
- Track referral requests

**Success Rate**:
- Cold application: 2-5%
- With referral: 30-50% (10-15x better!)

### 4. Resume Generator

**Purpose**: Create tailored resumes for each job

**Based on**: 29 Amazon/AWS employee resumes

**Features**:
- Impact-focused summaries
- Quantified achievements
- Categorized skills
- Company-specific "Why" section

## Technology Stack

### Core
- **Python 3.9+** - Main language
- **YAML** - Configuration files
- **JSON** - Data storage

### Web Scraping
- **Playwright** - Browser automation
- **httpx** - HTTP client
- **BeautifulSoup** (via Argus) - HTML parsing

### Resume Parsing
- **PyPDF2** - PDF parsing
- **python-docx** - DOCX parsing

### CLI
- **argparse** - Command-line interface
- **subprocess** - Process management

## Workflow Integration

### Interactive Mode

```
python3 interactive.py

1. Upload resume or enter manually
   ↓
2. Set preferences (titles, locations)
   ↓
3. Run discovery (287 jobs found)
   ↓
4. Run matching (95 matches)
   ↓
5. Find employees (LinkedIn links) ← NEW!
   ↓
6. Generate resumes (10 tailored)
   ↓
7. Apply with referrals
```

### Command-Line Mode

```bash
# Step 1: Discover
python3 jobbell.py discover
# → 287 jobs from 53 companies

# Step 2: Match
python3 jobbell.py match
# → 95 jobs scored 60%+

# Step 3: Find employees (NEW!)
python3 jobbell.py referral --top 10
# → LinkedIn links for top 10 companies

# Step 4: View
python3 jobbell.py show --top 20
# → Display top 20 matches

# Step 5: Generate resumes
python3 jobbell.py forge --top 10
# → 10 tailored resumes

# Step 6: Export
python3 jobbell.py export --output jobs.csv
# → CSV for tracking
```

## Scalability

### Current Capacity
- **Companies**: 53 (easily expandable)
- **Jobs per run**: 200-500
- **Processing time**: 5-10 minutes
- **Storage**: ~10MB per run

### Expansion Options
1. Add more companies (edit companies.yaml)
2. Add more ATS adapters
3. Improve scoring algorithm
4. Add more resume templates

## Security & Privacy

- **All data local** - Nothing sent to external servers
- **No API keys required** - Uses public career pages
- **Resume data private** - Stored only on your machine
- **LinkedIn links** - Opens in your browser, you control

## Future Enhancements

### Planned
- [ ] LLM integration for resume generation
- [ ] Application tracking system
- [ ] Email notifications for new matches
- [ ] Web UI dashboard
- [ ] Cover letter generation
- [ ] Interview preparation tips

### Possible
- [ ] LinkedIn API integration (requires auth)
- [ ] Auto-apply with referrals
- [ ] Salary data integration
- [ ] Company culture insights
- [ ] A/B test resume formats

---

**JobBell: Complete job search automation with referral system** 🔨
