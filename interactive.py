"""Interactive setup wizard for JobForge."""
import sys
import os
from pathlib import Path

# Set terminal title
sys.stdout.write("\033]0;Job Search\007")
sys.stdout.flush()


def run_interactive():
    """Run interactive setup wizard."""
    print("\n" + "="*70)
    print("🔨 Welcome to JobForge - Interactive Setup")
    print("="*70)
    
    # Step 1: Resume
    print("\n📄 Step 1: Resume")
    print("-" * 70)
    print("How would you like to provide your experience?")
    print("  1. Upload resume (PDF/DOCX)")
    print("  2. Enter career history manually")
    print("  3. Use existing career/ files")
    
    choice = input("\nChoice (1-3): ").strip()
    
    resume_path = None
    if choice == "1":
        resume_path = input("Enter resume path: ").strip()
        if not Path(resume_path).exists():
            print(f"❌ File not found: {resume_path}")
            return 1
        print(f"✅ Will parse: {resume_path}")
    elif choice == "2":
        print("\n📝 Let's build your career history...")
        create_career_interactive()
    else:
        print("✅ Using existing career/ files")
    
    # Step 2: Recent achievements
    print("\n🏆 Step 2: Recent Achievements (Optional)")
    print("-" * 70)
    print("Any recent achievements to highlight? (press Enter to skip)")
    
    achievements = []
    while True:
        achievement = input("Achievement (or Enter to continue): ").strip()
        if not achievement:
            break
        achievements.append(achievement)
    
    if achievements:
        print(f"✅ Added {len(achievements)} achievements")
    
    # Step 3: Job preferences
    print("\n🎯 Step 3: Job Preferences")
    print("-" * 70)
    
    titles = input("Target job titles (comma-separated): ").strip()
    locations = input("Preferred locations (comma-separated, or 'remote'): ").strip()
    
    # Save preferences
    save_preferences(titles, locations, achievements)
    
    # Step 4: Search options
    print("\n🔍 Step 4: Search Options")
    print("-" * 70)
    print("Where would you like to search for jobs?")
    print("  1. Top 53 companies (Automated - OpenAI, Google, Meta, etc.)")
    print("  2. ALL companies (Manual - LinkedIn, Indeed, Glassdoor, etc.)")
    print("  3. Both (Recommended)")
    
    search_choice = input("\nChoice (1-3): ").strip()
    
    # Step 5: Run workflow
    print("\n⚡ Step 5: Running JobForge...")
    print("="*70)
    
    if search_choice in ['1', '3']:
        print("\n🔍 Searching top 53 companies...")
        print("   (This may take 5-10 minutes)")
        # Discovery would run here
        print("   (Discovery integration pending - use Argus separately)")
    
    if search_choice in ['2', '3']:
        print("\n🌐 Generating search links for ALL companies...")
        import subprocess
        subprocess.run(['python3', 'jobforge.py', 'search', titles.split(',')[0].strip(), '--location', locations.split(',')[0].strip()])
    
    run_workflow(resume_path, search_choice, locations)
    
    print("\n✅ JobForge Complete!")
    print("\n📂 Check results:")
    print("   - results/matches/scored_jobs.csv")
    print("   - results/resumes/")
    
    return 0


def create_career_interactive():
    """Interactive career history builder."""
    print("\nCurrent/Most Recent Position:")
    title = input("  Job title: ").strip()
    company = input("  Company: ").strip()
    years = input("  Years (e.g., 2023-Present): ").strip()
    
    print("\nKey responsibilities (one per line, empty to finish):")
    responsibilities = []
    while True:
        resp = input("  - ").strip()
        if not resp:
            break
        responsibilities.append(resp)
    
    print("\nKey skills/technologies (comma-separated):")
    skills = input("  ").strip()
    
    # Save to career file
    year = "2024"
    content = f"""# {year} Work Experience

## {title} at {company} ({years})

### Responsibilities
{chr(10).join(f'- {r}' for r in responsibilities)}

### Technologies Used
{skills}
"""
    
    career_dir = Path('career')
    career_dir.mkdir(exist_ok=True)
    (career_dir / f'{year}.md').write_text(content)
    
    print(f"\n✅ Saved to career/{year}.md")


def save_preferences(titles, locations, achievements):
    """Save user preferences."""
    content = f"""# JobForge Settings (Auto-generated)

job_titles:
{chr(10).join(f'  - {t.strip()}' for t in titles.split(','))}

locations:
{chr(10).join(f'  - {l.strip()}' for l in locations.split(','))}

min_match_score: 60
"""
    
    if achievements:
        content += f"\n# Recent Achievements\n"
        content += "\n".join(f"# - {a}" for a in achievements)
    
    Path('config/settings.yaml').write_text(content)
    print("✅ Preferences saved")


def run_workflow(resume_path, search_choice, locations):
    """Run the JobForge workflow."""
    import subprocess
    
    # Discovery
    print("\n🔍 Discovering jobs...")
    if search_choice == "3" or "remote" in locations.lower():
        print("   Filtering for remote jobs...")
        # Will filter in matching step
    
    # For now, show what would happen
    print("   (Discovery integration pending - use Argus separately)")
    
    # Matching
    print("\n🎯 Matching jobs to your profile...")
    cmd = ['python3', 'jobforge.py', 'match']
    if resume_path:
        cmd.extend(['--resume', resume_path])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    
    # Show results
    print("\n📊 Top matches:")
    subprocess.run(['python3', 'jobforge.py', 'show', '--top', '10'])
    
    # Ask about employee search
    print("\n" + "="*70)
    print("💡 TIP: Referrals increase response rate by 10-15x!")
    print("="*70)
    print("\n🔍 Would you like to find employees at these companies?")
    print("   This helps you get referrals instead of cold applying.")
    print("")
    find_employees = input("Find employees for referrals? (y/n): ").strip().lower()
    
    if find_employees == 'y':
        print("\n🔍 Finding employees at top companies...")
        subprocess.run(['python3', 'core/referral/finder.py', '--top', '10'])
    
    # Ask about resume generation
    print("\n📄 Generate tailored resumes?")
    gen = input("Generate for top N matches (or 0 to skip): ").strip()
    
    if gen and gen != "0":
        print(f"\n🔨 Generating {gen} tailored resumes...")
        subprocess.run(['python3', 'jobforge.py', 'forge', '--top', gen])


if __name__ == '__main__':
    try:
        sys.exit(run_interactive())
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
        sys.exit(1)
