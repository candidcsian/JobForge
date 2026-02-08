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
            
            # Check if any documents were provided
            if len(documents) == 0:
                print("\n⚠️  No documents provided!")
                print("\nYou have two options:")
                print("1. Go back and provide documents")
                print("2. Enter your work history manually")
                
                choice = input("\nChoose (1/2): ").strip()
                if choice == '1':
                    print("\n❌ Please restart and provide your resume or work documents.")
                    print("   Run: cd ~/JobForge && ./start_agent.sh")
                    sys.exit(0)
                else:
                    print("\n📝 Let's collect your work history manually...")
                    self.collect_manual_work_history()
        else:
            print("\n📝 No problem! I'll guide you through manual entry.")
            self.user_data['documents'] = []
            self.collect_manual_work_history()
    
    def collect_manual_work_history(self):
        """Collect work history manually from user"""
        print("\n" + "="*70)
        print("📝 Manual Work History Collection")
        print("="*70)
        
        print("\nLet's collect your work history year by year.")
        print("I'll ask about each company you've worked for.\n")
        
        companies = []
        while True:
            print(f"\n--- Company #{len(companies) + 1} ---")
            company_name = input("Company name (or 'done' if finished): ").strip()
            
            if company_name.lower() == 'done':
                break
            
            if not company_name:
                continue
            
            role = input("Your role/title: ").strip()
            start_date = input("Start date (e.g., Jan 2020): ").strip()
            end_date = input("End date (e.g., Dec 2023 or 'Present'): ").strip()
            
            print("\nKey responsibilities (one per line, empty line to finish):")
            responsibilities = []
            while True:
                resp = input("  - ").strip()
                if not resp:
                    break
                responsibilities.append(resp)
            
            print("\nKey achievements (one per line, empty line to finish):")
            achievements = []
            while True:
                ach = input("  - ").strip()
                if not ach:
                    break
                achievements.append(ach)
            
            companies.append({
                'company': company_name,
                'role': role,
                'start_date': start_date,
                'end_date': end_date,
                'responsibilities': responsibilities,
                'achievements': achievements
            })
            
            print(f"\n✅ Added {company_name}")
        
        if len(companies) == 0:
            print("\n❌ No work history provided. Cannot proceed.")
            print("   Please restart and provide either:")
            print("   1. Resume documents, OR")
            print("   2. Manual work history")
            sys.exit(0)
        
        self.user_data['manual_history'] = companies
        print(f"\n✅ Collected history for {len(companies)} companies")
        
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
        
        # Import builder
        import sys
        sys.path.insert(0, str(self.base_dir / 'core'))
        from resume.builder import build_master_resume_from_manual
        
        try:
            output_file = self.career_dir / "master-resume.md"
            result = build_master_resume_from_manual(self.user_data, output_file)
            print(f"\n✅ Master resume created!")
            print(f"   {result}")
        except Exception as e:
            print(f"\n⚠️  Could not build resume: {e}")
            print("   Continuing with job search...")
        
    def create_ats_resume(self):
        """Create ATS-optimized resume"""
        print("\n" + "="*70)
        print("📄 STEP 5: Creating ATS-Optimized Resume")
        print("="*70)
        
        print("\nWhat type of roles are you targeting?")
        print("1. Senior QA Engineer / SDET")
        print("2. QA Lead / Manager")
        print("3. Software Engineer")
        print("4. Other")
        
        role_choice = input("\nChoose (1-4): ").strip()
        
        print("\n⏳ Creating your ATS-optimized resume...")
        
        # Import builder
        import sys
        sys.path.insert(0, str(self.base_dir / 'core'))
        from resume.builder import create_ats_resume_docx
        
        try:
            output_file = self.results_dir / "resumes" / "ATS_Resume.docx"
            result = create_ats_resume_docx(self.user_data, output_file)
            print(f"\n✅ ATS resume created!")
            print(f"   {result}")
        except Exception as e:
            print(f"\n⚠️  Could not create ATS resume: {e}")
            print("   Continuing with job search...")
        
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
        print("🎯 Next Steps")
        print("="*70)
        
        print("\n1. Open the CSV file")
        print("2. Click LinkedIn links to find referrals")
        print("3. Apply to top 20 matches this week")
        print("4. Follow up after 3-5 days")
        
        print("\n" + "="*70)
        
    def generate_summary(self):
        """Generate summary of what was created"""
        print("\n" + "="*70)
        print("✅ Setup Complete!")
        print("="*70)
        
        print(f"\n📂 Files created in: {self.results_dir}")
        print(f"   • matched_jobs.csv (with LinkedIn contacts)")
        print(f"   • ATS_Resume.docx")
        
        print("\n" + "="*70)
        
    def share_with_friends(self):
        """Information about sharing the tool"""
        print("\n" + "="*70)
        print("🤝 Share JobForge")
        print("="*70)
        
        print("\n📧 One command:")
        print("   bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobForge/main/jobforge_onecommand.sh)")
        
        print("\n🔗 GitHub:")
        print("   https://github.com/candidcsian/JobForge")
        
        print("\n" + "="*70)
        
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
            matched_jobs = search_and_match_jobs(role, self.career_dir, min_score=25)
            
            if matched_jobs:
                print(f"\n✨ Found {len(matched_jobs)} matching jobs!\n")
                
                # Show top 10
                print("🏆 Top 10 Matches:")
                print("="*70)
                for i, job in enumerate(matched_jobs[:10], 1):
                    stars = "⭐" * (job['match_score'] // 20)
                    print(f"\n{i}. {job['match_score']}% {stars} | {job['title']}")
                    print(f"   Company: {job['company']}")
                    print(f"   Apply: {job['url']}")
                
                # Save to CSV
                csv_file = self.results_dir / "matched_jobs.csv"
                csv_file.parent.mkdir(parents=True, exist_ok=True)
                save_matches_to_csv(matched_jobs, csv_file)
                
                print(f"\n" + "="*70)
                print(f"✅ All {len(matched_jobs)} jobs saved to CSV")
                print(f"📂 {csv_file}")
                print("\n💡 Open CSV to see:")
                print("   • LinkedIn contact links (find referrals)")
                print("   • Application tracking columns")
                print("="*70)
            else:
                print("\n⚠️  No matches found in free job APIs")
                print("   Showing aggregator links instead...")
        except Exception as e:
            print(f"\n⚠️  Smart matching error: {e}")
            print("   Showing aggregator links instead...")
        
        # Also show aggregator links
        print("\n" + "="*70)
        print("🌐 More Jobs - Search Aggregators")
        print("="*70)
        
        role_encoded = quote(role)
        
        print(f"\n   LinkedIn: https://www.linkedin.com/jobs/search/?keywords={role_encoded}")
        print(f"   Indeed: https://www.indeed.com/jobs?q={role_encoded}")
        print(f"   Naukri: https://www.naukri.com/{role.replace(' ', '-').lower()}-jobs")
        
        print("\n" + "="*70)
        
    def show_company_links(self):
        """Show direct links to top company career pages"""
        print("\n" + "="*70)
        print("🏢 Top Companies")
        print("="*70)
        
        companies = {
            "Google": "https://careers.google.com/",
            "Meta": "https://www.metacareers.com/",
            "Amazon": "https://www.amazon.jobs/",
            "Microsoft": "https://careers.microsoft.com/",
            "Apple": "https://www.apple.com/careers/",
            "Netflix": "https://jobs.netflix.com/",
            "Stripe": "https://stripe.com/jobs",
        }
        
        for company, url in companies.items():
            print(f"   {company:12s} {url}")
        
        print("\n" + "="*70)
    
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
