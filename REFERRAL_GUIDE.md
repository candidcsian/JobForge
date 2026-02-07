# 🤝 JobForge Referral System

## Why Referrals Matter

**Cold Application**: 2-5% response rate
**With Referral**: 30-50% response rate
**Referrals are 10-15x more effective!**

## How It Works

### 1. Find Matching Jobs
```bash
cd ~/JobForge
source venv/bin/activate

python3 jobforge.py discover
python3 jobforge.py match
```

### 2. Find Employees at Target Companies
```bash
python3 jobforge.py referral --top 10
```

**Output:**
```
1. Anthropic (3 matching jobs)
   🔗 Find employees: [LinkedIn link]
   🔗 Find engineers: [LinkedIn link]
   🔗 Find recruiters: [LinkedIn link]
   📄 Open roles:
      • Software Engineer (95%)
      • ML Engineer (87%)
```

### 3. Connect on LinkedIn

Click the links and look for:
- **2nd degree connections** (easier to reach)
- **People with similar background** (more likely to help)
- **Recent joiners** (enthusiastic about company)

### 4. Send Connection Request

**Template:**
```
Hi [Name],

I saw you work at [Company]. I'm interested in the [Role] 
position and would love to learn more about your experience 
there. Would you be open to a quick chat?

Best regards,
[Your Name]
```

### 5. Ask for Referral (After Connecting)

**Template:**
```
Hi [Name],

Thanks for connecting! I've applied to the [Role] position 
at [Company].

Quick background: [Your 1-2 line summary]

Would you be comfortable referring me? Happy to share my 
resume and discuss why I'm excited about this opportunity.

Best regards,
[Your Name]
```

## Complete Workflow

```bash
# Interactive mode (easiest)
python3 interactive.py

# When prompted:
# "Find employees for referrals? (y/n): y"
# → Automatically shows LinkedIn links
```

## Commands

```bash
# Find employees at top 10 companies
python3 jobforge.py referral --top 10

# Find employees at top 20 companies
python3 jobforge.py referral --top 20

# Results saved to:
# results/matches/[date]/employee_search.json
```

## Tips for Success

### 1. Personalize Your Message
❌ Generic: "Can you refer me?"
✅ Personal: "I saw your post about ML at OpenAI. I'm working on similar problems..."

### 2. Make It Easy
- Attach your resume
- Mention specific role and job ID
- Explain why you're a good fit (2-3 bullets)

### 3. Follow Up
- Wait 3-5 days
- Send polite follow-up
- Don't be pushy

### 4. Say Thank You
- Always thank them
- Keep them updated
- Offer to help them in future

## Example: Full Process

**Sarah (laid off from Amazon) looking for ML Engineer role:**

```bash
# 1. Find jobs
python3 jobforge.py discover
python3 jobforge.py match

# Output: 95 matching jobs, top is OpenAI ML Engineer (95%)

# 2. Find employees
python3 jobforge.py referral --top 5

# Output: LinkedIn links for OpenAI employees

# 3. On LinkedIn:
# - Found John (2nd degree connection, ex-Amazon, now at OpenAI)
# - Sent connection request with note
# - John accepted

# 4. Message John:
"Hi John,

Thanks for connecting! I saw you also worked at Amazon before 
joining OpenAI. I'm interested in the ML Engineer position 
(Job ID: 12345).

Quick background:
• 5+ years building ML systems at Amazon
• Led recommendation engine serving 10M+ users
• Strong Python, TensorFlow, AWS experience

Would you be comfortable referring me? Happy to share my resume 
and discuss why I'm excited about OpenAI's mission.

Best,
Sarah"

# 5. John refers Sarah
# 6. Sarah applies with referral code
# 7. Gets interview in 1 week (vs 2-5% chance cold)
```

## Success Metrics

Track your referral requests:
- Connections sent: 20
- Connections accepted: 15 (75%)
- Referrals received: 8 (40%)
- Interviews: 4 (50% of referrals)

**Much better than cold applying!**

## Message Templates

All templates available in `core/referral/messages.py`:
- Connection request
- Referral request
- Follow-up
- Thank you

## Integration with JobForge

```bash
# Full workflow
python3 interactive.py

# Steps:
1. Upload resume ✅
2. Find matching jobs ✅
3. Find employees ✅ (NEW!)
4. Generate tailored resumes ✅
5. Apply with referrals ✅
```

---

**Referrals + Tailored Resumes = Maximum Success!** 🤝
