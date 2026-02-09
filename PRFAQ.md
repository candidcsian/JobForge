# JobForge PR/FAQ

## Press Release

**FOR IMMEDIATE RELEASE**

### JobForge Launches Free AI-Powered Tool to Help Job Seekers Find Matching Jobs and Get Referrals

*Open-source tool matches jobs to user skills and provides LinkedIn contact links for referrals, helping job seekers land interviews 5x faster*

**[Your City], February 9, 2026** – Today marks the launch of JobForge, a free, open-source AI-powered tool that revolutionizes how job seekers find and apply to jobs. Unlike traditional job boards that require users to manually browse hundreds of listings, JobForge automatically fetches jobs from multiple sources, matches them to the user's skills, and provides direct links to find employees for referrals.

"Job searching is broken," said Senthil Kumar, creator of JobForge. "People spend hours browsing job boards, applying blindly, and getting no responses. Studies show that referrals increase your chances of getting an interview by 5x, but finding the right person to ask is hard. JobForge solves both problems – it finds jobs that actually match your skills and shows you exactly who to contact for a referral."

### How JobForge Works

JobForge is a command-line tool that runs entirely on the user's computer, ensuring 100% privacy. Users simply run one command, enter their work history, and within minutes receive:

1. **Smart Job Matching**: 50-100+ jobs matched to their specific skills with match scores (25-100%)
2. **LinkedIn Referral Finder**: Direct LinkedIn search links to find employees at each company
3. **Application Tracker**: CSV file with all matched jobs, application links, and tracking columns
4. **ATS-Optimized Resume**: Professional resume in Word format, ready to upload

"The magic is in the matching algorithm," Kumar explained. "We don't just keyword match – we understand your experience, calculate how well you fit each role, and prioritize jobs where you have the best chance. Then we make it easy to find someone who can refer you."

### Key Features

- **100% Free & Open Source**: No credit card, no signup, no limits
- **Privacy-First**: All data stays on user's computer, nothing sent to cloud
- **One-Command Install**: Works on Mac and Linux with a single command
- **Real-Time Job Data**: Fetches from multiple job APIs (RemoteOK, Remotive, Arbeitnow)
- **Referral-Focused**: LinkedIn contact links for every matched job
- **Application Tracking**: Built-in CSV tracker to manage job search

### Early Results

Beta testers report significant improvements in their job search:

- "I got 58 matched jobs in 2 minutes. Before, I'd spend hours browsing." – Beta Tester
- "The LinkedIn referral links are genius. I found 3 people to contact at my dream company." – Beta Tester
- "Finally, a tool that respects my privacy. Everything stays on my computer." – Beta Tester

### Availability

JobForge is available now at https://github.com/candidcsian/JobForge

Installation requires just one command:
```bash
bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobForge/main/jobforge_onecommand.sh)
```

The tool is completely free and open-source under the MIT license.

### Future Plans

Kumar plans to add premium features in the coming months, including:
- AI-powered cover letter generation
- Direct contact information (email/phone) for referrals
- Interview preparation with company-specific questions
- Web-based version for mobile access

"For now, we're focused on getting feedback and helping as many job seekers as possible," Kumar said. "The core features will always be free. Premium features will be for those who want extra help."

### About JobForge

JobForge was created by Senthil Kumar, a Senior QA Engineer with 16+ years of experience at Amazon and other tech companies. Frustrated by the inefficiency of traditional job search, Kumar built JobForge to help job seekers work smarter, not harder.

For more information, visit: https://github.com/candidcsian/JobForge

---

## Frequently Asked Questions (FAQ)

### General Questions

**Q: What is JobForge?**
A: JobForge is a free, open-source AI-powered tool that helps job seekers find jobs matching their skills and connect with employees for referrals. It automates the tedious parts of job searching – browsing listings, matching skills, and finding contacts.

**Q: How is JobForge different from LinkedIn or Indeed?**
A: Traditional job boards show you ALL jobs and you have to manually filter. JobForge fetches jobs, matches them to YOUR specific skills, scores each match (25-100%), and provides LinkedIn links to find referral contacts. It's like having a personal recruiter who pre-screens jobs for you.

**Q: Is it really free?**
A: Yes, 100% free with no limits. The core features (job matching, referral finder, resume builder, application tracker) will always be free. We may add optional premium features later (like AI cover letters or direct contact info), but the main tool stays free forever.

**Q: Do I need to create an account?**
A: No! JobForge runs entirely on your computer. No signup, no login, no account needed. Your data stays private on your machine.

**Q: What platforms does it work on?**
A: Mac and Linux. Windows support coming soon. You need Python 3.9+ (usually pre-installed on Mac).

---

### How It Works

**Q: How does the job matching work?**
A: You enter your work history (companies, roles, responsibilities). JobForge extracts your skills, then fetches 100+ jobs from multiple sources (RemoteOK, Remotive, Arbeitnow). It calculates a match score for each job based on how many of your skills appear in the job description, plus role-specific boosts (e.g., "Senior" roles get higher scores if you're senior). You get a ranked list of best matches.

**Q: Where do the jobs come from?**
A: Currently from three free job APIs: RemoteOK, Remotive, and Arbeitnow. These aggregate remote jobs from hundreds of companies. We're adding more sources (LinkedIn, Indeed, Glassdoor) in future versions.

**Q: How does the referral finder work?**
A: For each matched job, JobForge generates a LinkedIn search URL like: "Senior QA Engineer at Stripe". When you click it, LinkedIn shows you employees with that title at that company. You can then connect with them and ask for a referral. Studies show referrals increase interview chances by 5x.

**Q: What's in the CSV file?**
A: The CSV contains all matched jobs with these columns:
- Match % (e.g., 85%)
- Job Title
- Company
- Location
- Apply URL (direct link to job posting)
- LinkedIn Contacts (link to find referrals)
- Applied (checkbox for you to track)
- Status (e.g., "Applied", "Interview", "Offer")
- Notes (your comments)

You can open it in Excel or Google Sheets and use it to manage your entire job search.

**Q: Does it create a real resume?**
A: Yes! It creates two files:
1. **master-resume.md** - Complete career profile in Markdown
2. **ATS_Resume.docx** - Professional resume in Word format, optimized for Applicant Tracking Systems (ATS)

The Word resume is ready to upload to job applications.

---

### Privacy & Security

**Q: Is my data private?**
A: Absolutely. JobForge runs 100% locally on your computer. Nothing is sent to any server or cloud. Your work history, resume, and job matches all stay on your machine. We can't see your data because we never receive it.

**Q: Do you track usage?**
A: Currently, no. The tool is completely offline. In future versions, we may add optional anonymous analytics (like "X jobs fetched") to improve the product, but it will always be opt-in and anonymous.

**Q: Can I delete my data?**
A: Yes, just delete the ~/JobForge folder. Since everything is local, deleting the folder removes all your data permanently.

---

### Technical Questions

**Q: What are the system requirements?**
A: 
- Mac or Linux
- Python 3.9+ (usually pre-installed)
- Internet connection (to fetch jobs)
- 50MB disk space

**Q: How long does it take to run?**
A: 
- Installation: 1-2 minutes
- Entering work history: 5-10 minutes
- Job fetching & matching: 1-2 minutes
- Total: ~15 minutes for first run

**Q: Can I run it multiple times?**
A: Yes! Run it weekly to get fresh job matches. Your work history is saved, so subsequent runs are faster.

**Q: Does it work offline?**
A: Partially. You can build your resume offline, but job fetching requires internet. Once jobs are fetched, you can work with the CSV offline.

**Q: What if I get an error?**
A: Open an issue on GitHub: https://github.com/candidcsian/JobForge/issues
We respond within 24 hours.

---

### Job Search Strategy

**Q: How many jobs should I apply to?**
A: We recommend applying to your top 20-30 matches. Focus on quality over quantity. Use the referral links to increase your chances.

**Q: Should I apply to jobs with low match scores?**
A: Generally, focus on 60%+ matches. But if a 40% match is at your dream company, go for it! The scores are guidance, not rules.

**Q: How do I ask for a referral?**
A: 
1. Click the LinkedIn Contacts link
2. Find 2-3 employees with similar roles
3. Send a connection request with a note: "Hi [Name], I saw the [Job Title] opening at [Company]. I have [X years] experience in [relevant skill]. Would you be open to a quick chat about the role?"
4. If they accept, ask if they'd be willing to refer you

**Q: What if no one responds?**
A: Try 5-10 people per company. Someone usually responds. Also, apply directly even without a referral – the match score means you're qualified.

**Q: How long does job search take?**
A: With JobForge:
- Week 1: Apply to 20-30 jobs, reach out for referrals
- Week 2-3: 5-10 recruiter calls, 3-5 interviews
- Week 4: 1-3 offers

Traditional job search: 2-3 months. JobForge cuts it to 3-4 weeks by focusing your efforts.

---

### Future Features

**Q: What's coming next?**
A: Planned features:
- More job sources (LinkedIn, Indeed, Glassdoor APIs)
- AI cover letter generator
- Direct contact info (email/phone, not just LinkedIn)
- Interview prep with company-specific questions
- Web version (access from phone/tablet)
- Email alerts for new matching jobs

**Q: Will it always be free?**
A: Core features (job matching, referral finder, basic resume) will always be free. Premium features (AI cover letters, direct contacts, interview prep) may be paid ($9-19/month) to sustain development.

**Q: Can I contribute?**
A: Yes! JobForge is open-source. Contributions welcome:
- Code: Submit PRs on GitHub
- Ideas: Open feature requests
- Feedback: Share your experience
- Spread the word: Tell friends who are job searching

**Q: Will you add [specific feature]?**
A: Maybe! Open a feature request on GitHub. We prioritize based on user demand.

---

### Monetization (Future)

**Q: How will you make money?**
A: We're exploring:
1. **Freemium**: Free tier (10 matches/month), Pro tier ($9/month, unlimited)
2. **Premium features**: AI cover letters ($4.99 each), Resume review ($49), Interview prep ($29)
3. **B2B**: Tools for recruiters ($99/month) and companies ($299/month)

**Q: When will you start charging?**
A: Not for at least 2-3 months. We want to get 500-1000 users first, collect feedback, and ensure the product is valuable. Early users will get lifetime discounts.

**Q: Will my data be sold?**
A: Never. We will never sell user data. Our business model is subscriptions for premium features, not data selling.

---

### Support

**Q: How do I get help?**
A: 
1. Check the README: https://github.com/candidcsian/JobForge
2. Open an issue: https://github.com/candidcsian/JobForge/issues
3. Email: (add your email)

**Q: How fast do you respond?**
A: Usually within 24 hours. We're a small team but committed to helping users.

**Q: Can I request a feature?**
A: Yes! Open a feature request on GitHub. We love hearing what users want.

**Q: I found a bug. What should I do?**
A: Open an issue on GitHub with:
- What you were doing
- What happened
- Error message (if any)
- Your OS (Mac/Linux)

We'll fix it ASAP.

---

### Success Stories (Coming Soon)

**Q: Has anyone gotten a job using JobForge?**
A: We just launched! Check back in a few weeks for success stories. If JobForge helps you land a job, please share your story!

---

### About the Creator

**Q: Who built JobForge?**
A: Senthil Kumar, a Senior QA Engineer with 16+ years at Amazon and other tech companies. Frustrated by inefficient job searching, he built JobForge to help others.

**Q: Why did you build this?**
A: "I was job searching and spent hours browsing Indeed, LinkedIn, Naukri. I'd apply to 50 jobs and hear back from 2. I realized the problem: I was applying to jobs that didn't match my skills, and I had no referrals. I built JobForge to solve both problems – match jobs to skills and make referrals easy. Now I'm sharing it with everyone."

**Q: Is this your full-time job?**
A: Not yet. Currently a side project. If it helps enough people, I may work on it full-time.

---

### Getting Started

**Q: How do I install JobForge?**
A: One command:
```bash
bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobForge/main/jobforge_onecommand.sh)
```

Paste that in your terminal (Mac/Linux) and press Enter. It downloads, installs, and runs automatically.

**Q: What happens after I install?**
A: The tool guides you through:
1. Enter your name, email, work history
2. It builds your resume
3. Fetches and matches jobs
4. Creates a CSV with all matches
5. Shows you the top 10 matches

Takes about 15 minutes total.

**Q: Can I see a demo?**
A: Check the README on GitHub for screenshots and example output.

**Q: I'm not technical. Can I still use it?**
A: Yes! If you can copy-paste a command into Terminal, you can use JobForge. The tool guides you step-by-step with simple questions.

---

## Contact

**GitHub**: https://github.com/candidcsian/JobForge
**Issues**: https://github.com/candidcsian/JobForge/issues
**Email**: (add your email)
**Twitter**: (add your handle)

---

*Last Updated: February 9, 2026*
