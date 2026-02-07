"""Matching engine - scores jobs against user profile."""
import json
from pathlib import Path
from datetime import datetime


def run_matching(args):
    """Run job matching."""
    print("🎯 JobForge - Job Matching")
    print("="*50)
    
    # Check for career history or resume
    career_dir = Path(args.career_dir)
    if not career_dir.exists():
        print(f"\n❌ Career directory not found: {career_dir}")
        print("\nCreate career history files:")
        print("  career/2024.md")
        print("  career/2023.md")
        return 1
    
    # Parse career history
    print(f"\n📂 Loading career history from: {career_dir}")
    career_files = list(career_dir.glob('*.md'))
    print(f"   Found {len(career_files)} career files")
    
    # Extract profile
    profile = extract_profile_from_career(career_files)
    print(f"\n📊 Profile Summary:")
    print(f"   Skills: {len(profile['skills'])} identified")
    print(f"   Titles: {len(profile['titles'])} identified")
    print(f"   Experience: ~{profile['years']} years")
    
    # Load jobs
    jobs_dir = Path('results/jobs')
    if not jobs_dir.exists():
        print(f"\n❌ No jobs found. Run discovery first:")
        print("   python jobforge.py discover")
        return 1
    
    jobs = load_all_jobs(jobs_dir)
    print(f"\n🔍 Found {len(jobs)} jobs to analyze")
    
    if not jobs:
        print("\n❌ No jobs to match. Run discovery first.")
        return 1
    
    # Check for remote-only filter
    remote_only = any('remote' in loc.lower() for loc in profile.get('locations', []))
    
    # Score jobs (simplified for now)
    print(f"\n⚡ Scoring jobs (min score: {args.min_score})...")
    if remote_only:
        print("   🌍 Filtering for remote jobs only")
    scored = score_jobs_simple(jobs, profile, args.min_score, remote_only)
    
    print(f"\n✨ Found {len(scored)} matching jobs")
    
    # Save results
    output_dir = Path(args.output) / datetime.now().strftime('%Y-%m-%d')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    save_results(scored, output_dir)
    
    # Show top 10
    print(f"\n🏆 Top 10 Matches:")
    print("="*70)
    for i, job in enumerate(scored[:10], 1):
        stars = "⭐⭐⭐" if job['score'] >= 80 else "⭐⭐" if job['score'] >= 60 else "⭐"
        print(f"\n{i}. {job['company']} - {job['title']}")
        print(f"   Score: {job['score']}% {stars}")
        print(f"   {job['url']}")
    
    print(f"\n✅ Results saved to: {output_dir}")
    return 0


def extract_profile_from_career(career_files):
    """Extract skills and experience from career markdown files."""
    skills = set()
    titles = set()
    
    tech_keywords = {
        'python', 'java', 'javascript', 'typescript', 'go', 'rust',
        'react', 'node', 'django', 'flask', 'fastapi',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes',
        'postgresql', 'mongodb', 'redis', 'sql',
        'tensorflow', 'pytorch', 'machine learning', 'ml', 'ai'
    }
    
    for file in career_files:
        content = file.read_text().lower()
        
        # Extract skills
        for keyword in tech_keywords:
            if keyword in content:
                skills.add(keyword)
        
        # Extract titles from headers
        for line in content.split('\n'):
            if '##' in line and ('engineer' in line or 'scientist' in line or 'developer' in line):
                title = line.replace('#', '').strip()
                if ' at ' in title:
                    title = title.split(' at ')[0].strip()
                titles.add(title.title())
    
    # Estimate years (count files as years)
    years = len(career_files)
    
    return {
        'skills': list(skills),
        'titles': list(titles),
        'years': years,
        'locations': []  # Will be populated from settings
    }


def load_all_jobs(jobs_dir):
    """Load all jobs from results directory."""
    jobs = []
    for json_file in jobs_dir.rglob('jobs.json'):
        try:
            with open(json_file) as f:
                jobs.extend(json.load(f))
        except:
            pass
    return jobs


def score_jobs_simple(jobs, profile, min_score, remote_only=False):
    """Simple scoring algorithm."""
    scored = []
    
    for job in jobs:
        title = job.get('title', '').lower()
        location = job.get('location', '').lower()
        
        # Filter remote jobs if requested
        if remote_only:
            if 'remote' not in location:
                continue
        
        score = 0
        
        # Title match (40 points)
        if any(t.lower() in title for t in profile['titles']):
            score += 40
        
        # Skills match (40 points)
        matched_skills = [s for s in profile['skills'] if s in title]
        if matched_skills:
            score += min(40, len(matched_skills) * 10)
        
        # Experience (20 points)
        if 'senior' in title and profile['years'] >= 3:
            score += 20
        elif 'staff' not in title and 'principal' not in title:
            score += 15
        
        # Bonus for remote (5 points)
        if 'remote' in location:
            score += 5
        
        if score >= min_score:
            scored.append({
                **job,
                'score': score,
                'matched_skills': matched_skills,
                'is_remote': 'remote' in location
            })
    
    return sorted(scored, key=lambda x: x['score'], reverse=True)


def save_results(scored, output_dir):
    """Save scored results."""
    # JSON
    with open(output_dir / 'scored_jobs.json', 'w') as f:
        json.dump(scored, f, indent=2)
    
    # CSV
    with open(output_dir / 'scored_jobs.csv', 'w') as f:
        f.write('Score,Company,Title,Location,URL\n')
        for job in scored:
            f.write(f"{job['score']},\"{job.get('company', '')}\",\"{job.get('title', '')}\",\"{job.get('location', '')}\",{job.get('url', '')}\n")
