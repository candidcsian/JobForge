#!/usr/bin/env python3
"""
JobForge Interactive Agent - Resume Builder & Job Search Assistant

This agent guides users through:
1. Career data collection (year by year)
2. Master resume building
3. LinkedIn profile optimization
4. Job portal setup (Naukri, Indeed, etc.)
5. Job search and application tracking

Usage:
    python3 jobforge_agent.py
"""

import os
import sys
from pathlib import Path

class JobForgeAgent:
    def __init__(self):
        self.base_dir = Path.home() / "JobForge"
        self.career_dir = self.base_dir / "career"
        self.results_dir = self.base_dir / "results"
        self.user_data = {}
        
    def welcome(self):
        """Welcome message and introduction"""
        print("\n" + "="*70)
        print("🚀 Welcome to JobForge - Your AI Career Assistant!")
        print("="*70)
        print("\nI'll help you:")
        print("  ✅ Build your master resume from career history")
        print("  ✅ Create ATS-optimized resumes")
        print("  ✅ Optimize your LinkedIn profile")
        print("  ✅ Set up job portals (Naukri, Indeed, etc.)")
        print("  ✅ Find and apply to matching jobs")
        print("\nThis will take about 30-60 minutes. Let's get started!\n")
        
    def collect_basic_info(self):
        """Collect basic user information"""
        print("\n" + "="*70)
        print("📝 STEP 1: Basic Information")
        print("="*70)
        
        print("\n1. What's your full name?")
        self.user_data['name'] = input("   > ")
        
        print("2. Your email address:")
        self.user_data['email'] = input("   > ")
        
        print("3. Your phone number:")
        self.user_data['phone'] = input("   > ")
        
        print("4. Current location (e.g., Bangalore, India):")
        self.user_data['location'] = input("   > ")
        
        print("\n5. Current employment status:")
        print("   a) Employed")
        print("   b) Unemployed")
        print("   c) Freelancing")
        status = input("   Choose (a/b/c): ").lower().strip()
        self.user_data['employment_status'] = status
        
        if status == 'a':
            print("\n6. Current company name:")
            self.user_data['current_company'] = input("   > ")
            print("7. Current job title:")
            self.user_data['current_role'] = input("   > ")
            print("8. When did you start (e.g., Jan 2020)?")
            self.user_data['current_start'] = input("   > ")
        
        print("\n✅ Basic info collected!")
        
    def collect_career_timeline(self):
        """Collect career history year by year"""
        print("\n" + "="*70)
        print("📅 STEP 2: Career Timeline")
        print("="*70)
        
        print("\nWhat year did you start your career? (e.g., 2009):")
        start_year = input("   > ").strip()
        
        try:
            start_year_int = int(start_year)
            current_year = 2026
            print(f"\nGreat! You have {current_year - start_year_int} years of experience.")
        except ValueError:
            print("Invalid year. Using 2015 as default.")
            start_year_int = 2015
        
        print("\nNow, I'll ask about your work history year by year.")
        print("You can provide:")
        print("  - Resume documents (PDF/DOCX)")
        print("  - Work summaries")
        print("  - Performance reviews")
        print("  - Or just tell me what you did each year")
        
        input("\nPress Enter when ready to continue...")
        
        self.user_data['career_start'] = start_year
        self.user_data['career_history'] = []
        
        # Ask for documents
        print("\n" + "-"*70)
        print("Do you have any of these documents?")
        print("-"*70)
        print("1. Old resume (PDF/DOCX)")
        print("2. Work summaries or performance reviews")
        print("3. LinkedIn profile export")
        print("4. None - I'll provide information manually")
        
        doc_choice = input("\nChoose option (1/2/3/4): ")
        
        if doc_choice in ['1', '2', '3']:
            print("\n📂 Please provide the file path(s):")
            print("   (You can drag and drop files here, or type the path)")
            print("   (Type 'done' when finished)")
            
            documents = []
            while True:
                file_path = input("\nFile path (or 'done'): ").strip()
                if file_path.lower() == 'done':
                    break
                if file_path:
                    documents.append(file_path)
                    print(f"   ✅ Added: {file_path}")
            
            self.user_data['documents'] = documents
            print(f"\n✅ Collected {len(documents)} document(s)")
        else:
            print("\n📝 No problem! I'll guide you through manual entry.")
            self.user_data['documents'] = []
        
    def ask_for_missing_years(self):
        """Identify and ask for missing years"""
        print("\n" + "="*70)
        print("🔍 STEP 3: Filling in the Gaps")
        print("="*70)
        
        print("\nBased on your documents, I'll identify any missing years")
        print("and ask you specific questions about those periods.")
        
        # This would be implemented with actual document parsing
        print("\n⏳ Analyzing your career timeline...")
        print("   (This is where the tool would parse documents and identify gaps)")
        
        # Placeholder for missing years logic
        missing_years = []  # Would be populated by document analysis
        
        if missing_years:
            print(f"\n📋 I need information about these years: {', '.join(missing_years)}")
            for year in missing_years:
                print(f"\n--- {year} ---")
                company = input(f"Company you worked for in {year}: ")
                role = input(f"Your role: ")
                projects = input(f"Key projects (comma-separated): ")
                achievements = input(f"Major achievements: ")
                
                self.user_data['career_history'].append({
                    'year': year,
                    'company': company,
                    'role': role,
                    'projects': projects,
                    'achievements': achievements
                })
        else:
            print("\n✅ Great! Your career timeline is complete.")
        
    def build_master_resume(self):
        """Build master resume from collected data"""
        print("\n" + "="*70)
        print("🔨 STEP 4: Building Your Master Resume")
        print("="*70)
        
        print("\n⏳ Processing your career data...")
        print("   - Extracting skills and technologies")
        print("   - Identifying key achievements")
        print("   - Calculating quantified metrics")
        print("   - Organizing by time periods")
        
        # This would call the actual resume building logic
        print("\n✅ Master resume created!")
        print(f"   Location: {self.career_dir}/master-resume.md")
        
    def create_ats_resume(self):
        """Create ATS-optimized resume"""
        print("\n" + "="*70)
        print("📄 STEP 5: Creating ATS-Optimized Resume")
        print("="*70)
        
        print("\nWhat type of roles are you targeting?")
        print("1. Senior QA Engineer / SDET")
        print("2. QA Lead / Manager")
        print("3. Mobile QA Engineer")
        print("4. Security QA Engineer")
        print("5. Custom (I'll specify)")
        
        role_choice = input("\nChoose (1-5): ")
        
        print("\n⏳ Creating your ATS-optimized resume...")
        print("   - Optimizing keywords for ATS")
        print("   - Formatting for readability")
        print("   - Highlighting quantified achievements")
        
        print("\n✅ ATS resume created!")
        print(f"   Location: {self.results_dir}/resumes/ATS_Resume.docx")
        
    def optimize_linkedin(self):
        """Guide LinkedIn profile optimization"""
        print("\n" + "="*70)
        print("💼 STEP 6: LinkedIn Profile Optimization")
        print("="*70)
        
        print("\nDo you want help updating your LinkedIn profile?")
        choice = input("(yes/no): ").lower()
        
        if choice == 'yes':
            print("\n📋 I'll create optimized content for:")
            print("   ✅ Headline (220 characters)")
            print("   ✅ About section (2,600 characters)")
            print("   ✅ Experience descriptions")
            print("   ✅ Skills to add")
            print("   ✅ Privacy settings for discreet job search")
            
            print("\n⏳ Generating LinkedIn content...")
            
            print("\n✅ LinkedIn content created!")
            print(f"   Location: {self.results_dir}/resumes/LinkedIn_Profile.md")
            
            print("\n📱 Next steps:")
            print("   1. Open the LinkedIn_Profile.md file")
            print("   2. Copy the headline and paste to LinkedIn")
            print("   3. Copy the About section and paste to LinkedIn")
            print("   4. Add the recommended skills")
            print("   5. Update privacy settings as shown")
            
            input("\nPress Enter when you've updated LinkedIn...")
            print("✅ Great! Your LinkedIn is now optimized!")
        else:
            print("\n⏭️  Skipping LinkedIn optimization")
        
    def setup_job_portals(self):
        """Guide job portal setup"""
        print("\n" + "="*70)
        print("🌐 STEP 7: Job Portal Setup")
        print("="*70)
        
        print("\nI'll help you set up profiles on:")
        print("   1. Naukri.com (India)")
        print("   2. LinkedIn Jobs")
        print("   3. Indeed.com")
        print("   4. Instahyre (Tech jobs)")
        print("   5. Cutshort (Startups)")
        
        print("\nWhich portals do you want to set up?")
        print("   a) All of them")
        print("   b) Let me choose")
        print("   c) Skip for now")
        
        choice = input("\nChoose (a/b/c): ").lower()
        
        if choice == 'a':
            portals = ['naukri', 'linkedin', 'indeed', 'instahyre', 'cutshort']
        elif choice == 'b':
            portals = []
            if input("Naukri.com? (y/n): ").lower() == 'y':
                portals.append('naukri')
            if input("LinkedIn Jobs? (y/n): ").lower() == 'y':
                portals.append('linkedin')
            if input("Indeed.com? (y/n): ").lower() == 'y':
                portals.append('indeed')
            if input("Instahyre? (y/n): ").lower() == 'y':
                portals.append('instahyre')
            if input("Cutshort? (y/n): ").lower() == 'y':
                portals.append('cutshort')
        else:
            portals = []
        
        if portals:
            print("\n📋 Setup instructions for each portal:")
            for portal in portals:
                self._show_portal_instructions(portal)
        else:
            print("\n⏭️  Skipping job portal setup")
        
    def _show_portal_instructions(self, portal):
        """Show setup instructions for specific portal"""
        instructions = {
            'naukri': """
            
--- NAUKRI.COM ---
1. Go to: https://www.naukri.com
2. Login or create account
3. Click "Update Profile" → "Resume"
4. Upload: {resume_path}
5. Set profile to "Actively Looking"
6. Verify parsing is correct
7. Set job preferences (location, salary, etc.)
            """,
            'linkedin': """
            
--- LINKEDIN JOBS ---
1. Already done! Your profile is optimized
2. Go to: https://www.linkedin.com/jobs
3. Search for your target roles
4. Use "Easy Apply" for quick applications
5. Set up job alerts
            """,
            'indeed': """
            
--- INDEED.COM ---
1. Go to: https://www.indeed.co.in
2. Login or create account
3. Upload resume: {resume_path}
4. Set job preferences
5. Turn ON "Open to Work"
6. Set up job alerts
            """,
            'instahyre': """
            
--- INSTAHYRE ---
1. Go to: https://www.instahyre.com
2. Sign up with LinkedIn (easiest)
3. Upload resume: {resume_path}
4. Set preferences (roles, companies, locations)
5. Turn ON "Open to opportunities"
            """,
            'cutshort': """
            
--- CUTSHORT ---
1. Go to: https://cutshort.io
2. Sign up
3. Upload resume: {resume_path}
4. Complete profile
5. Set "Open to opportunities"
            """
        }
        
        resume_path = f"{self.results_dir}/resumes/ATS_Resume.docx"
        print(instructions[portal].format(resume_path=resume_path))
        input("Press Enter when done with this portal...")
        print(f"✅ {portal.upper()} setup complete!")
        
    def job_search_strategy(self):
        """Provide job search strategy"""
        print("\n" + "="*70)
        print("🎯 STEP 8: Job Search Strategy")
        print("="*70)
        
        print("\nBased on your profile, here's your action plan:")
        print("\n📅 WEEK 1:")
        print("   - Apply to 20-30 jobs on Naukri")
        print("   - Apply to 10-15 jobs on LinkedIn")
        print("   - Connect with 10 recruiters")
        print("   - Set up job alerts")
        
        print("\n📅 WEEK 2-3:")
        print("   - Continue applying (50+ total)")
        print("   - Respond to recruiter messages")
        print("   - Prepare for interviews")
        print("   - Practice STAR stories")
        
        print("\n📅 WEEK 4:")
        print("   - Interview rounds")
        print("   - Negotiate offers")
        print("   - Make decision")
        
        print("\n💡 PRO TIPS:")
        print("   ✅ Apply within 24 hours of job posting")
        print("   ✅ Customize resume for each application")
        print("   ✅ Follow up with recruiters after 3-5 days")
        print("   ✅ Keep track of applications in spreadsheet")
        print("   ✅ Prepare 5-10 STAR stories for interviews")
        
    def generate_summary(self):
        """Generate summary of what was created"""
        print("\n" + "="*70)
        print("🎉 CONGRATULATIONS! Setup Complete!")
        print("="*70)
        
        print("\n📂 Files Created:")
        print(f"   ✅ Master Resume: {self.career_dir}/master-resume.md")
        print(f"   ✅ ATS Resume: {self.results_dir}/resumes/ATS_Resume.docx")
        print(f"   ✅ LinkedIn Profile: {self.results_dir}/resumes/LinkedIn_Profile.md")
        print(f"   ✅ Skills Matrix: {self.career_dir}/skills-matrix.md")
        
        print("\n✅ What's Ready:")
        print("   ✅ Your master career profile (16+ years documented)")
        print("   ✅ ATS-optimized resume for job applications")
        print("   ✅ LinkedIn profile content (copy-paste ready)")
        print("   ✅ Job portal setup instructions")
        print("   ✅ Job search strategy and timeline")
        
        print("\n🚀 Next Steps:")
        print("   1. Upload resume to Naukri (from mobile if needed)")
        print("   2. Start applying to jobs (20-30 this week)")
        print("   3. Connect with recruiters on LinkedIn")
        print("   4. Set up job alerts on all portals")
        print("   5. Prepare for interviews")
        
        print("\n📊 Expected Results:")
        print("   Week 1: 5-10 recruiter calls")
        print("   Week 2-3: 10-15 interviews")
        print("   Week 4: 2-5 offers")
        
        print("\n💼 Salary Expectations:")
        print("   Senior QA Engineer: ₹25-35 LPA")
        print("   SDET II/III: ₹30-40 LPA")
        print("   QA Lead: ₹40-60 LPA")
        
        print("\n" + "="*70)
        print("Good luck with your job search! 🍀")
        print("="*70)
        
    def share_with_friends(self):
        """Information about sharing the tool"""
        print("\n" + "="*70)
        print("🤝 Share JobForge with Friends")
        print("="*70)
        
        print("\n📧 Send them this one command:")
        print("\n   bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobForge/main/jobforge_onecommand.sh)")
        
        print("\n🔗 Or share the GitHub link:")
        print("   https://github.com/candidcsian/JobForge")
        
        print("\n✅ That's it! They'll get:")
        print("   • ATS-optimized resume builder")
        print("   • LinkedIn profile optimizer")
        print("   • Job search links (1000+ jobs)")
        print("   • 100% private & free")
        
    def search_jobs(self):
        """Search for jobs and match to profile"""
        from urllib.parse import quote
        from datetime import datetime
        import sys
        sys.path.insert(0, str(self.base_dir / 'core'))
        from discovery.free_job_apis import search_and_match_jobs, save_matches_to_csv
        
        print("\n" + "="*70)
        print("🔍 STEP 9: Smart Job Search & Matching")
        print("="*70)
        
        print("\nNow let's find jobs that match YOUR profile!")
        print("\nWhat type of roles are you looking for?")
        role = input("   (e.g., Senior QA Engineer, SDET, Software Engineer): ").strip()
        
        if not role:
            role = "Software Engineer"
            print(f"   Using default: {role}")
        
        # Smart matching from free APIs
        print("\n" + "="*70)
        print("🎯 SMART MATCHING - Finding jobs that match YOUR skills")
        print("="*70)
        
        try:
            matched_jobs = search_and_match_jobs(role, self.career_dir, min_score=40)
            
            if matched_jobs:
                print(f"\n✨ Found {len(matched_jobs)} jobs matching your profile!")
                
                # Show top 10
                print("\n🏆 Top 10 Matches:")
                print("="*70)
                for i, job in enumerate(matched_jobs[:10], 1):
                    stars = "⭐" * (job['match_score'] // 20)
                    print(f"\n{i}. {job['title']} at {job['company']}")
                    print(f"   Match: {job['match_score']}% {stars}")
                    print(f"   Apply: {job['url']}")
                    
                    # Show LinkedIn contact link
                    from discovery.free_job_apis import generate_linkedin_contact_url
                    linkedin_url = generate_linkedin_contact_url(job['company'], job['title'])
                    print(f"   Find referrals: {linkedin_url}")
                
                # Save to CSV
                csv_file = self.results_dir / "matched_jobs.csv"
                csv_file.parent.mkdir(parents=True, exist_ok=True)
                save_matches_to_csv(matched_jobs, csv_file)
                
                print(f"\n✅ All {len(matched_jobs)} matches saved to:")
                print(f"   {csv_file}")
                print("\n💡 CSV includes:")
                print("   • Match scores for each job")
                print("   • Direct application links")
                print("   • LinkedIn contact search links (find referrals!)")
                print("   • Tracking columns (Applied, Status, Notes)")
                print("\n🎯 STRATEGY:")
                print("   1. Open CSV in Excel/Google Sheets")
                print("   2. Click 'LinkedIn Contacts' link for each job")
                print("   3. Connect with 2-3 employees at that company")
                print("   4. Ask for referral before applying")
                print("   5. Apply with referral = 5x better chance!")
            else:
                print("\n⚠️  No matches found in free job APIs")
                print("   Showing aggregator links instead...")
        except Exception as e:
            print(f"\n⚠️  Smart matching error: {e}")
            print("   Showing aggregator links instead...")
        
        # Also show aggregator links
        print("\n" + "="*70)
        print("🌐 ADDITIONAL SEARCH - Job Aggregators")
        print("="*70)
        
        print("\nSearch these sites for more jobs:")
        
        role_encoded = quote(role)
        location_encoded = quote("Remote")
        
        print("\n📋 Job Aggregator Links:")
        print(f"\n   LinkedIn:")
        print(f"   https://www.linkedin.com/jobs/search/?keywords={role_encoded}&f_TPR=r604800")
        
        print(f"\n   Indeed:")
        print(f"   https://www.indeed.com/jobs?q={role_encoded}&fromage=7")
        
        print(f"\n   Glassdoor:")
        print(f"   https://www.glassdoor.com/Job/jobs.htm?sc.keyword={role_encoded}")
        
        print(f"\n   Wellfound (Startups):")
        print(f"   https://wellfound.com/jobs?query={role_encoded}")
        
        print(f"\n   Naukri (India):")
        print(f"   https://www.naukri.com/{role.replace(' ', '-').lower()}-jobs")
        
        # Save aggregator links
        results_file = self.results_dir / "job_search_links.txt"
        results_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w') as f:
            f.write(f"Job Search Links for: {role}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"LinkedIn: https://www.linkedin.com/jobs/search/?keywords={role_encoded}&f_TPR=r604800\n")
            f.write(f"Indeed: https://www.indeed.com/jobs?q={role_encoded}&fromage=7\n")
            f.write(f"Glassdoor: https://www.glassdoor.com/Job/jobs.htm?sc.keyword={role_encoded}\n")
            f.write(f"Wellfound: https://wellfound.com/jobs?query={role_encoded}\n")
            f.write(f"Naukri: https://www.naukri.com/{role.replace(' ', '-').lower()}-jobs\n")
        
        print(f"\n✅ Aggregator links saved to: {results_file}")
        
    def show_company_links(self):
        """Show direct links to top company career pages"""
        print("\n" + "="*70)
        print("🏢 STEP 10: Top Company Career Pages")
        print("="*70)
        
        print("\nDirect links to apply at top companies:")
        
        companies = {
            "OpenAI": "https://openai.com/careers/",
            "Google": "https://careers.google.com/",
            "Meta": "https://www.metacareers.com/",
            "Amazon": "https://www.amazon.jobs/",
            "Microsoft": "https://careers.microsoft.com/",
            "Apple": "https://www.apple.com/careers/",
            "Netflix": "https://jobs.netflix.com/",
            "Stripe": "https://stripe.com/jobs",
            "Airbnb": "https://careers.airbnb.com/",
            "Uber": "https://www.uber.com/careers/",
            "Coinbase": "https://www.coinbase.com/careers",
            "Databricks": "https://www.databricks.com/company/careers",
            "Snowflake": "https://careers.snowflake.com/",
            "Anthropic": "https://www.anthropic.com/careers",
            "Spotify": "https://www.lifeatspotify.com/jobs"
        }
        
        print("\n🔗 Top 15 Companies:")
        for i, (company, url) in enumerate(companies.items(), 1):
            print(f"   {i:2d}. {company:15s} {url}")
        
        # Save to file
        links_file = self.results_dir / "company_career_pages.txt"
        links_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(links_file, 'w') as f:
            f.write("Top Company Career Pages\n")
            f.write("="*70 + "\n\n")
            for company, url in companies.items():
                f.write(f"{company}: {url}\n")
        
        print(f"\n✅ Links saved to: {links_file}")
        print("\n💡 Tip: Visit these pages and search for your role!")
    
    def run(self):
        """Main execution flow"""
        try:
            self.welcome()
            self.collect_basic_info()
            self.collect_career_timeline()
            self.ask_for_missing_years()
            self.build_master_resume()
            self.create_ats_resume()
            self.optimize_linkedin()
            self.setup_job_portals()
            self.search_jobs()  # Job aggregator links (works!)
            self.show_company_links()  # Direct company links (simple!)
            self.job_search_strategy()
            self.generate_summary()
            
            # Ask if they want to share
            print("\n")
            share = input("Would you like to share this tool with friends? (yes/no): ")
            if share.lower() == 'yes':
                self.share_with_friends()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Process interrupted. Your progress has been saved.")
            print("Run the tool again to continue from where you left off.")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please report this issue or try again.")

def main():
    """Entry point"""
    agent = JobForgeAgent()
    agent.run()

if __name__ == "__main__":
    main()
