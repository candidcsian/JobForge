# 🤖 AI Interview Coach

**NEW FEATURE:** Get personalized interview preparation plans for your matched jobs!

---

## ✨ What You Get

For each matched job, AI Interview Coach generates:

### 1. **Match Explanation**
- **Why you're a good fit** (3 specific reasons with evidence)
- **What to emphasize** in your application
- **Potential gaps** and how to address them positively
- **Action steps** with deadlines

### 2. **2-Week Prep Plan**
Day-by-day schedule covering:
- **Week 1:** Application, STAR stories, company research, technical review
- **Week 2:** Follow-ups, deep dives, mock interviews, final prep

Each day includes:
- Focus area
- Time estimate
- Detailed checklist
- Success criteria

### 3. **Periodic Check-ins**
- **Day 3:** Applied? Found referrals? Started prep?
- **Day 7:** Research done? Stories ready? Mock interview?
- **Day 11:** Final review? Tech setup? Ready to go?

### 4. **Interview Resources**
- **STAR story templates** for your experience
- **Company research guide** (what to look for)
- **Common questions** with answer frameworks
- **Technical topics** to review

---

## 📊 Example Output

```json
{
  "why_you_match": [
    {
      "reason": "Your 5 years in fintech aligns with their payment platform",
      "evidence": "Amazon Pay Later, Wealth products",
      "strength": "high"
    }
  ],
  
  "what_to_emphasize": [
    "Lead with: Reduced post-launch defects by 35%",
    "Highlight: Zero Sev-1 issues at Brazil launch",
    "Mention: CI/CD pipeline automation experience"
  ],
  
  "prep_plan": {
    "week_1": {
      "day_1": {
        "task": "Apply + find referrals",
        "checklist": [
          "Tailor resume",
          "Find 3 employees on LinkedIn",
          "Send connection requests",
          "Apply on company website"
        ]
      }
    }
  },
  
  "checkins": [
    {
      "day": 3,
      "message": "How's prep going? Applied yet?"
    }
  ]
}
```

---

## 🎯 How It Works

1. **Run JobForge** - Get matched jobs
2. **Choose AI Prep** - When prompted, say "yes"
3. **Get Plans** - Receives prep plan for top 5 matches
4. **Follow Schedule** - Day-by-day guidance
5. **Track Progress** - Check-ins keep you accountable

---

## 📂 Output Files

Plans saved to: `~/JobForge/results/interview_prep/`

Each file contains:
- `interview_prep_CompanyName.json`

Open in any text editor or JSON viewer.

---

## 💡 Pro Tips

### **Use the Prep Plan:**
- ✅ Follow day-by-day (don't skip ahead)
- ✅ Check off items as you complete them
- ✅ Adjust timeline if interview scheduled sooner
- ✅ Focus on high-strength matches first

### **STAR Stories:**
- **S**ituation: Set the context
- **T**ask: What needed to be done
- **A**ction: What YOU did (be specific)
- **R**esult: Quantified outcome

### **Company Research:**
- Recent news (last 6 months)
- Product launches
- Challenges/opportunities
- Culture/values

---

## 🚀 Future Enhancements

Coming soon:
- **AI-powered STAR story generator** (from your resume)
- **Mock interview simulator** (practice with AI)
- **Real-time feedback** on your answers
- **Company-specific questions** (based on Glassdoor data)
- **Salary negotiation coach**

---

## 💰 Pricing (Future)

**Currently:** FREE (beta)

**Planned:**
- **Free:** Top 3 matches
- **Pro ($9/month):** Top 10 matches
- **Premium ($19/month):** Unlimited + mock interviews

---

## 🤝 Feedback

This is a NEW feature! Please share feedback:
- What's helpful?
- What's missing?
- What would you pay for?

Open an issue on GitHub or email us.

---

**Built with ❤️ to help you ace interviews!**
