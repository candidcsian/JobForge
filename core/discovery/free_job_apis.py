"""Fetch jobs from free job APIs and match to user profile."""
import httpx
import json
from pathlib import Path
from datetime import datetime
import re


def fetch_remoteok_jobs(keywords=None):
    """Fetch jobs from RemoteOK API (free, no auth needed)."""
    try:
        url = "https://remoteok.com/api"
        headers = {'User-Agent': 'JobForge/1.0'}
        
        response = httpx.get(url, headers=headers, timeout=30)
        jobs = response.json()[1:]  # First item is metadata
        
        # Filter by keywords if provided
        if keywords:
            kw_lower = keywords.lower()
            jobs = [j for j in jobs if kw_lower in j.get('position', '').lower() 
                    or kw_lower in j.get('description', '').lower()]
        
        return [{
            'title': j.get('position'),
            'company': j.get('company'),
            'location': 'Remote',
            'url': j.get('url'),
            'description': j.get('description', ''),
            'tags': j.get('tags', []),
            'source': 'RemoteOK'
        } for j in jobs[:100]]  # Limit to 100
    except Exception as e:
        print(f"   ⚠️  RemoteOK error: {e}")
        return []


def fetch_remotive_jobs(keywords=None):
    """Fetch jobs from Remotive API (free, no auth needed)."""
    try:
        url = "https://remotive.com/api/remote-jobs"
        response = httpx.get(url, timeout=30)
        data = response.json()
        jobs = data.get('jobs', [])
        
        # Filter by keywords
        if keywords:
            kw_lower = keywords.lower()
            jobs = [j for j in jobs if kw_lower in j.get('title', '').lower() 
                    or kw_lower in j.get('description', '').lower()]
        
        return [{
            'title': j.get('title'),
            'company': j.get('company_name'),
            'location': 'Remote',
            'url': j.get('url'),
            'description': j.get('description', ''),
            'tags': j.get('tags', []),
            'source': 'Remotive'
        } for j in jobs[:100]]
    except Exception as e:
        print(f"   ⚠️  Remotive error: {e}")
        return []


def extract_skills_from_profile(career_dir):
    """Extract skills from user's career files."""
    skills = set()
    career_path = Path(career_dir)
    
    # Read all career files
    for file in career_path.glob('*-master.md'):
        content = file.read_text()
        
        # Extract skills section
        if '## Skills' in content or '## Technical Skills' in content:
            skills_section = re.search(r'## (?:Technical )?Skills.*?(?=##|\Z)', content, re.DOTALL)
            if skills_section:
                text = skills_section.group(0)
                # Extract words that look like skills
                words = re.findall(r'\b[A-Z][a-zA-Z+#\.]{2,}\b', text)
                skills.update(words)
    
    # Also check skills matrix
    for file in career_path.glob('*skills*.md'):
        content = file.read_text()
        words = re.findall(r'\b[A-Z][a-zA-Z+#\.]{2,}\b', content)
        skills.update(words)
    
    return list(skills)


def calculate_match_score(job, user_skills):
    """Calculate match score between job and user skills."""
    job_text = f"{job['title']} {job['description']}".lower()
    
    matches = 0
    for skill in user_skills:
        if skill.lower() in job_text:
            matches += 1
    
    # Score based on percentage of skills matched
    if user_skills:
        score = int((matches / len(user_skills)) * 100)
    else:
        score = 50  # Default if no skills extracted
    
    # Boost score if title matches common roles
    title_lower = job['title'].lower()
    if any(word in title_lower for word in ['senior', 'lead', 'engineer', 'developer']):
        score = min(100, score + 10)
    
    return score, matches


def search_and_match_jobs(keywords, career_dir, min_score=40):
    """Search jobs and match to user profile."""
    print("\n🔍 Fetching jobs from free APIs...")
    print("   • RemoteOK (remote jobs)")
    print("   • Remotive (remote jobs)")
    
    # Fetch jobs
    all_jobs = []
    all_jobs.extend(fetch_remoteok_jobs(keywords))
    all_jobs.extend(fetch_remotive_jobs(keywords))
    
    print(f"\n✅ Found {len(all_jobs)} jobs")
    
    if not all_jobs:
        return []
    
    # Extract user skills
    print(f"\n📊 Analyzing your profile from: {career_dir}")
    user_skills = extract_skills_from_profile(career_dir)
    print(f"   Identified {len(user_skills)} skills: {', '.join(user_skills[:10])}...")
    
    # Score each job
    print(f"\n⚡ Matching jobs to your profile (min score: {min_score}%)...")
    matched_jobs = []
    
    for job in all_jobs:
        score, skill_matches = calculate_match_score(job, user_skills)
        if score >= min_score:
            job['match_score'] = score
            job['matched_skills'] = skill_matches
            matched_jobs.append(job)
    
    # Sort by score
    matched_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    
    return matched_jobs


def save_matches_to_csv(jobs, output_file):
    """Save matched jobs to CSV."""
    import csv
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Match %', 'Title', 'Company', 'Location', 'Source', 
            'URL', 'Applied', 'Status', 'Notes'
        ])
        
        for job in jobs:
            writer.writerow([
                f"{job['match_score']}%",
                job['title'],
                job['company'],
                job['location'],
                job['source'],
                job['url'],
                '',  # Applied (user fills)
                '',  # Status (user fills)
                ''   # Notes (user fills)
            ])


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python free_job_apis.py 'keywords'")
        sys.exit(1)
    
    keywords = sys.argv[1]
    career_dir = Path('career')
    
    jobs = search_and_match_jobs(keywords, career_dir)
    
    print(f"\n✨ Found {len(jobs)} matching jobs")
    
    # Show top 10
    print("\n🏆 Top 10 Matches:")
    for i, job in enumerate(jobs[:10], 1):
        print(f"\n{i}. {job['title']} at {job['company']}")
        print(f"   Match: {job['match_score']}% | {job['source']}")
        print(f"   {job['url']}")
