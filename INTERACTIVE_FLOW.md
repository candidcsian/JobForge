# 🎯 JobBell - Interactive Mode Flow

## What Happens When You Run

```bash
python3 interactive.py
```

## Complete Flow with User Prompts

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    🔨 Welcome to JobBell - Interactive Setup             ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│ 📄 Step 1: Resume                                                        │
├─────────────────────────────────────────────────────────────────────────┤
│ How would you like to provide your experience?                          │
│   1. Upload resume (PDF/DOCX)                                           │
│   2. Enter career history manually                                      │
│   3. Use existing career/ files                                         │
│                                                                          │
│ Choice (1-3): _                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 🏆 Step 2: Recent Achievements (Optional)                               │
├─────────────────────────────────────────────────────────────────────────┤
│ Any recent achievements to highlight? (press Enter to skip)             │
│                                                                          │
│ Achievement (or Enter to continue): _                                   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 🎯 Step 3: Job Preferences                                              │
├─────────────────────────────────────────────────────────────────────────┤
│ Target job titles (comma-separated): _                                  │
│ Preferred locations (comma-separated, or 'remote'): _                   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 🔍 Step 4: Search Options                                               │
├─────────────────────────────────────────────────────────────────────────┤
│ Where would you like to search for jobs?                                │
│   1. Top 53 companies (Automated - OpenAI, Google, Meta, etc.)         │
│   2. ALL companies (Manual - LinkedIn, Indeed, Glassdoor, etc.)        │
│   3. Both (Recommended)                                                 │
│                                                                          │
│ Choice (1-3): _                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ ⚡ Step 5: Running JobBell...                                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│ If Choice 1 or 3:                                                       │
│   🔍 Searching top 53 companies...                                      │
│   → Found 287 jobs                                                      │
│                                                                          │
│ If Choice 2 or 3:                                                       │
│   🌐 Generating search links for ALL companies...                       │
│   → LinkedIn Jobs: [link]                                               │
│   → Indeed: [link]                                                      │
│   → Glassdoor: [link]                                                   │
│   → Wellfound: [link]                                                   │
│   → Y Combinator: [link]                                                │
│                                                                          │
│ 🎯 Matching jobs to your profile...                                     │
│   → 95 matches found (60%+ score)                                       │
│                                                                          │
│ 📊 Top matches:                                                         │
│   1. OpenAI - ML Engineer (95%)                                         │
│   2. Anthropic - Senior SDE (87%)                                       │
│   3. Google - Staff Engineer (78%)                                      │
│   ...                                                                    │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 💡 TIP: Referrals increase response rate by 10-15x!                     │
├─────────────────────────────────────────────────────────────────────────┤
│ 🔍 Would you like to find employees at these companies?                 │
│    This helps you get referrals instead of cold applying.               │
│                                                                          │
│ Find employees for referrals? (y/n): _                                 │
│                                                                          │
│ If yes:                                                                  │
│   🔍 Finding employees at top companies...                              │
│   → LinkedIn links generated for 10 companies                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 📄 Generate tailored resumes?                                           │
├─────────────────────────────────────────────────────────────────────────┤
│ Generate for top N matches (or 0 to skip): _                           │
│                                                                          │
│ If N > 0:                                                                │
│   🔨 Generating N tailored resumes...                                   │
│   → 10 resumes generated                                                │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ ✅ JobBell Complete!                                                   │
├─────────────────────────────────────────────────────────────────────────┤
│ 📂 Check results:                                                       │
│    - results/matches/scored_jobs.csv                                    │
│    - results/matches/ACTION_SHEET.csv                                   │
│    - results/resumes/                                                   │
│                                                                          │
│ 💡 Next steps:                                                          │
│    1. Open ACTION_SHEET.csv in Excel                                    │
│    2. Click LinkedIn links to find employees                            │
│    3. Get referrals                                                     │
│    4. Apply with tailored resumes                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Example Session

```
User Input:
-----------
Step 1: Choice 1 (Upload resume)
        Path: ~/Downloads/my-resume.pdf

Step 2: Achievement 1: "Led team of 5 engineers"
        Achievement 2: "Reduced latency by 60%"
        Achievement 3: [Enter - skip]

Step 3: Titles: "Machine Learning Engineer, Senior Software Engineer"
        Locations: "Remote, California"

Step 4: Choice 3 (Both - Recommended)

Step 5: [Automatic processing]

Step 6: Find employees? y

Step 7: Generate resumes? 10


Output:
-------
✅ 287 jobs found from 53 companies
✅ LinkedIn/Indeed/Glassdoor links generated
✅ 95 jobs matched (60%+)
✅ LinkedIn links for 10 companies
✅ 10 tailored resumes generated
✅ ACTION_SHEET.csv created

Files created:
- results/matches/2026-02-04/ACTION_SHEET.csv
- results/matches/2026-02-04/scored_jobs.csv
- results/matches/2026-02-04/employee_search.json
- results/resumes/openai-ml-engineer.md
- results/resumes/anthropic-senior-sde.md
- ... (8 more resumes)
```

## What Each Choice Does

### Step 4: Search Options

**Choice 1: Top 53 companies (Automated)**
```
✅ Searches: OpenAI, Google, Meta, Amazon, Stripe, etc.
✅ Time: 5-10 minutes
✅ Output: 200-500 jobs in structured format
✅ Matching: Automatic scoring
✅ Best for: Quick, high-quality results
```

**Choice 2: ALL companies (Manual)**
```
✅ Searches: LinkedIn, Indeed, Glassdoor, Wellfound, YC
✅ Time: Instant (generates links)
✅ Output: Links to millions of jobs
✅ Matching: Manual browsing
✅ Best for: Exploring beyond top companies
```

**Choice 3: Both (Recommended)**
```
✅ Combines both approaches
✅ Automated search of 53 companies
✅ Plus links to ALL companies
✅ Best coverage
✅ Best for: Comprehensive job search
```

## Time Breakdown

```
Total Time: 30 minutes (one-time setup)

Step 1: Resume upload          - 2 minutes
Step 2: Achievements           - 3 minutes
Step 3: Preferences            - 2 minutes
Step 4: Search choice          - 1 minute
Step 5: Processing (automated) - 10 minutes
Step 6: Employee finder        - 5 minutes
Step 7: Resume generation      - 7 minutes

Result: Complete job search setup in 30 minutes!
```

## Weekly Routine (After Setup)

```
Week 2+: 1 hour/week

Monday (10 min):
  python3 jobbell.py discover
  → New jobs found

Tuesday (10 min):
  python3 jobbell.py match
  python3 jobbell.py show --top 20
  → Review new matches

Wednesday (10 min):
  python3 jobbell.py referral --top 10
  → Get LinkedIn links, connect with people

Thursday (10 min):
  python3 jobbell.py forge --top 10
  → Generate new resumes

Friday (20 min):
  → Apply to top 10 with referrals
```

---

**Interactive mode = Complete setup in 30 minutes!** 🎯
