# 📊 JobBell Output Files - Complete Guide

## What You Get After Running JobBell

### 1. ACTION_SHEET.csv - Your Main Tracking File ⭐

**Location**: `results/matches/2026-02-04/ACTION_SHEET.csv`

**Open in Excel/Google Sheets and you'll see:**

| Priority | Score | Company | Job Title | Location | Job URL | Resume File | LinkedIn - Employees | LinkedIn - Engineers | Status | Referral Contact | Applied Date | Notes |
|----------|-------|---------|-----------|----------|---------|-------------|---------------------|---------------------|--------|-----------------|--------------|-------|
| 1 | 95% | OpenAI | ML Engineer | Remote | [Apply Link] | openai-ml-engineer.md | [LinkedIn Link] | [LinkedIn Link] | TODO | | | |
| 2 | 87% | Anthropic | Senior SDE | Remote | [Apply Link] | anthropic-senior-sde.md | [LinkedIn Link] | [LinkedIn Link] | TODO | | | |
| 3 | 78% | Google | Staff Engineer | Mountain View | [Apply Link] | google-staff-engineer.md | [LinkedIn Link] | [LinkedIn Link] | TODO | | | |

**How to Use:**
1. Open in Excel/Google Sheets
2. Click LinkedIn links to find employees
3. Update "Status" column as you progress:
   - TODO → CONTACTED → APPLIED → INTERVIEW → OFFER
4. Fill in "Referral Contact" when you get referrals
5. Track "Applied Date" for follow-ups

### 2. scored_jobs.csv - Simple List

**Location**: `results/matches/2026-02-04/scored_jobs.csv`

```csv
Score,Company,Title,Location,URL
95,OpenAI,ML Engineer,Remote,https://jobs.ashbyhq.com/openai/ml-123
87,Anthropic,Senior SDE,Remote,https://boards.greenhouse.io/anthropic/sde-456
78,Google,Staff Engineer,Mountain View,https://careers.google.com/jobs/789
```

### 3. employee_search.json - LinkedIn Links

**Location**: `results/matches/2026-02-04/employee_search.json`

```json
[
  {
    "company": "OpenAI",
    "jobs_count": 3,
    "linkedin_all": "https://www.linkedin.com/search/results/people/?currentCompany=OpenAI",
    "linkedin_engineers": "https://www.linkedin.com/search/results/people/?currentCompany=OpenAI&keywords=engineer",
    "linkedin_recruiters": "https://www.linkedin.com/search/results/people/?currentCompany=OpenAI&keywords=recruiter",
    "top_jobs": [
      {"title": "ML Engineer", "score": 95, "url": "..."}
    ]
  }
]
```

### 4. Tailored Resumes - One per Job

**Location**: `results/resumes/`

```
results/resumes/
├── openai-ml-engineer.md          ← Use this for OpenAI
├── anthropic-senior-sde.md        ← Use this for Anthropic
├── google-staff-engineer.md       ← Use this for Google
├── meta-senior-qa.md
├── amazon-sde.md
└── ... (10 total)
```

## 📋 Complete Workflow with Files

### Step 1: Generate Everything
```bash
cd ~/JobBell
source venv/bin/activate

python3 jobbell.py discover
python3 jobbell.py match
python3 jobbell.py referral --top 10
python3 jobbell.py forge --top 10
python3 core/cli/action_sheet.py
```

### Step 2: Open ACTION_SHEET.csv
```bash
# Mac
open results/matches/2026-02-04/ACTION_SHEET.csv

# Or copy to desktop
cp results/matches/2026-02-04/ACTION_SHEET.csv ~/Desktop/
```

### Step 3: Use the Action Sheet

**Example: Applying to OpenAI**

1. **Find Employee** (Row 1, Column 8)
   - Click LinkedIn link
   - Find John (ex-Amazon, now at OpenAI)
   - Send connection request

2. **Get Referral**
   - Message John: "Would you refer me?"
   - John says yes
   - Update sheet: Referral Contact = "John Smith"

3. **Apply** (Row 1, Column 6)
   - Click Job URL
   - Upload resume from Column 7: `openai-ml-engineer.md`
   - Submit with referral code

4. **Track** (Row 1, Columns 11-14)
   - Status: TODO → CONTACTED → APPLIED
   - Applied Date: 2026-02-05
   - Notes: "Referred by John Smith, ex-Amazon colleague"

## 📊 Visual Example

```
ACTION_SHEET.csv in Excel:

┌──────────┬───────┬───────────┬─────────────┬──────────┬─────────────┬──────────────────────┬─────────────────┬─────────┬──────────────────┬──────────────┬────────┐
│ Priority │ Score │ Company   │ Job Title   │ Location │ Job URL     │ Resume File          │ LinkedIn Link   │ Status  │ Referral Contact │ Applied Date │ Notes  │
├──────────┼───────┼───────────┼─────────────┼──────────┼─────────────┼──────────────────────┼─────────────────┼─────────┼──────────────────┼──────────────┼────────┤
│    1     │ 95%   │ OpenAI    │ ML Engineer │ Remote   │ [LINK]      │ openai-ml-engineer   │ [LINKEDIN]      │ APPLIED │ John Smith       │ 2026-02-05   │ Ex-AMZ │
│    2     │ 87%   │ Anthropic │ Senior SDE  │ Remote   │ [LINK]      │ anthropic-senior-sde │ [LINKEDIN]      │ CONTACT │ Sarah Lee        │              │ 2nd deg│
│    3     │ 78%   │ Google    │ Staff Eng   │ MTV      │ [LINK]      │ google-staff-eng     │ [LINKEDIN]      │ TODO    │                  │              │        │
└──────────┴───────┴───────────┴─────────────┴──────────┴─────────────┴──────────────────────┴─────────────────┴─────────┴──────────────────┴──────────────┴────────┘

✅ Click links directly in Excel
✅ Track progress in Status column
✅ Know which resume to use
✅ Track referrals and dates
```

## 🎯 Summary

**You get 4 main outputs:**

1. **ACTION_SHEET.csv** ⭐ - Everything in one place
   - Job details
   - LinkedIn links
   - Resume to use
   - Tracking columns

2. **scored_jobs.csv** - Simple job list

3. **employee_search.json** - LinkedIn links (JSON format)

4. **Tailored Resumes** - 10 customized resumes

**Best practice:** Use ACTION_SHEET.csv as your main tracking tool!

## 📝 Commands

```bash
# Generate action sheet
cd ~/JobBell
source venv/bin/activate
python3 core/cli/action_sheet.py

# Open it
open results/matches/*/ACTION_SHEET.csv

# Or copy to desktop
cp results/matches/*/ACTION_SHEET.csv ~/Desktop/my-job-search.csv
```

---

**One CSV with everything you need to apply!** 📊
