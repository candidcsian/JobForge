# 🌐 Search ALL Companies (Not Just 53)

## Two Approaches

### Approach 1: JobBell Direct (53 Companies)
```bash
python3 jobbell.py discover
```
**Pros**: Automated, structured data, ready for matching
**Cons**: Limited to 53 pre-configured companies

### Approach 2: Job Aggregators (ALL Companies)
```bash
python3 jobbell.py search "Machine Learning Engineer" --location "Remote"
```
**Pros**: Searches ALL companies, thousands of jobs
**Cons**: Manual browsing required

## How to Search ALL Companies

### Quick Command

```bash
cd ~/JobBell
source venv/bin/activate

# Search by role and location
python3 jobbell.py search "Software Engineer" --location "Remote"
python3 jobbell.py search "Data Scientist" --location "San Francisco"
python3 jobbell.py search "ML Engineer" --location "New York"
```

### What You Get

```
📋 Job Aggregator Links:

1. LinkedIn Jobs
   🔗 [Direct search link]
   💡 Best for tech roles, shows company size

2. Indeed
   🔗 [Direct search link]
   💡 Largest database, all industries

3. Glassdoor
   🔗 [Direct search link]
   💡 Includes salary info and reviews

4. Wellfound (AngelList)
   🔗 [Direct search link]
   💡 Best for startups

5. Y Combinator Jobs
   🔗 [Direct search link]
   💡 YC-backed startups only
```

## Complete Workflow

### Step 1: Search Aggregators (ALL Companies)
```bash
python3 jobbell.py search "ML Engineer" --location "Remote"
```

### Step 2: Browse Results
- Open all 5 links in browser
- Apply filters (date, remote, experience)
- Save interesting companies/jobs

### Step 3: Add Companies to JobBell
Found interesting companies? Add them:

```bash
vim config/companies.yaml

# Add at the end:
- name: NewCompany
  career_url: https://boards.greenhouse.io/newcompany
  ats_type: greenhouse
```

### Step 4: Run JobBell Discovery
```bash
python3 jobbell.py discover --companies "NewCompany"
```

### Step 5: Find Employees & Get Referrals
```bash
python3 jobbell.py referral --top 10
```

## Location-Based Search

### Remote Jobs
```bash
python3 jobbell.py search "Software Engineer" --location "Remote"
```

### Specific City
```bash
python3 jobbell.py search "Data Scientist" --location "San Francisco"
python3 jobbell.py search "ML Engineer" --location "New York"
python3 jobbell.py search "Backend Engineer" --location "Seattle"
```

### Multiple Locations
Run multiple searches:
```bash
python3 jobbell.py search "SWE" --location "Remote"
python3 jobbell.py search "SWE" --location "California"
python3 jobbell.py search "SWE" --location "New York"
```

## Job Aggregator Comparison

| Aggregator | Best For | Coverage | Features |
|------------|----------|----------|----------|
| **LinkedIn Jobs** | Tech roles | High | Company insights, connections |
| **Indeed** | All industries | Highest | Largest database |
| **Glassdoor** | Research | High | Salaries, reviews |
| **Wellfound** | Startups | Medium | Equity info, startup culture |
| **Y Combinator** | YC startups | Low | Early-stage, high growth |

## Advanced: Combine Both Approaches

### 1. Start with Aggregators (Broad Search)
```bash
python3 jobbell.py search "ML Engineer" --location "Remote"
# → Find 1000+ jobs across ALL companies
```

### 2. Identify Top Companies
Browse results, note companies you like:
- OpenAI, Anthropic, Scale AI (already in JobBell)
- NewStartup1, NewStartup2 (not in JobBell)

### 3. Add New Companies
```bash
vim config/companies.yaml
# Add NewStartup1, NewStartup2
```

### 4. Run Targeted Discovery
```bash
python3 jobbell.py discover
# → Now searches 55 companies (53 + 2 new)
```

### 5. Match & Apply
```bash
python3 jobbell.py match
python3 jobbell.py referral --top 10
python3 jobbell.py forge --top 10
```

## Example: Complete Search

**Sarah wants ML Engineer roles, Remote only**

```bash
# Step 1: Search ALL companies
python3 jobbell.py search "Machine Learning Engineer" --location "Remote"

# Step 2: Open all 5 aggregator links
# → Found 500+ jobs
# → Noted 10 interesting companies

# Step 3: Check which are already in JobBell
grep "name:" config/companies.yaml
# → 5 already there (OpenAI, Anthropic, etc.)
# → 5 new (Hugging Face, Cohere, etc.)

# Step 4: Add new companies
vim config/companies.yaml
# Added Hugging Face, Cohere, etc.

# Step 5: Run discovery on all
python3 jobbell.py discover
# → 287 jobs from 58 companies

# Step 6: Match to profile
python3 jobbell.py match
# → 95 matches

# Step 7: Find employees
python3 jobbell.py referral --top 10
# → LinkedIn links for top 10

# Step 8: Generate resumes
python3 jobbell.py forge --top 10
# → 10 tailored resumes

# Result: 10 high-quality applications with referrals
```

## Tips

### 1. Use Aggregators for Discovery
- Find companies you didn't know about
- See salary ranges
- Read company reviews

### 2. Use JobBell for Automation
- Automated crawling
- Smart matching
- Referral finding
- Resume generation

### 3. Best of Both Worlds
- Aggregators: Broad search (1000+ jobs)
- JobBell: Deep search (specific companies)
- Combine for maximum coverage

## Filters to Use on Aggregators

### LinkedIn Jobs
- Date posted: Past week
- Remote: Yes
- Experience level: Mid-Senior
- Company size: 51-200 (startups)

### Indeed
- Date: Last 7 days
- Job type: Full-time
- Remote: Yes
- Salary: $150k+

### Glassdoor
- Date: Last week
- Remote: Yes
- Company rating: 4.0+
- Salary: Show only

### Wellfound
- Remote: Yes
- Stage: Series A-C
- Equity: 0.1%+
- Team size: 10-50

## Summary

**For 53 Companies (Automated)**:
```bash
python3 jobbell.py discover
```

**For ALL Companies (Manual)**:
```bash
python3 jobbell.py search "Your Role" --location "Your Location"
```

**Best Strategy**: Use both!
1. Search aggregators for discovery
2. Add interesting companies to JobBell
3. Let JobBell automate the rest

---

**Search thousands of companies, apply to the best ones!** 🌐
