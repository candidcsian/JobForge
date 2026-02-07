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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        response = httpx.get(url, headers=headers, timeout=30, follow_redirects=True)
        data = response.json()
        
        # Skip first item (metadata)
        if isinstance(data, list) and len(data) > 0:
            jobs = data[1:] if isinstance(data[0], dict) and 'legal' in str(data[0]) else data
        else:
            jobs = []
        
        # Filter by keywords if provided
        if keywords:
            kw_lower = keywords.lower()
            filtered = []
            for j in jobs:
                if not isinstance(j, dict):
                    continue
                title = str(j.get('position', '')).lower()
                desc = str(j.get('description', '')).lower()
                tags = ' '.join(str(t) for t in j.get('tags', [])).lower()
                
                if kw_lower in title or kw_lower in desc or kw_lower in tags:
                    filtered.append(j)
            jobs = filtered
        
        result = []
        for j in jobs[:100]:
            if not isinstance(j, dict):
                continue
            result.append({
                'title': j.get('position', 'Unknown'),
                'company': j.get('company', 'Unknown'),
                'location': 'Remote',
                'url': j.get('url', ''),
                'description': j.get('description', ''),
                'tags': j.get('tags', []),
                'source': 'RemoteOK'
            })
        
        return result
    except Exception as e:
        print(f"   ⚠️  RemoteOK error: {e}")
        return []


def fetch_remotive_jobs(keywords=None):
    """Fetch jobs from Remotive API (free, no auth needed)."""
    try:
        url = "https://remotive.com/api/remote-jobs"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = httpx.get(url, headers=headers, timeout=30)
        data = response.json()
        jobs = data.get('jobs', [])
        
        # Filter by keywords
        if keywords:
            kw_lower = keywords.lower()
            filtered = []
            for j in jobs:
                title = str(j.get('title', '')).lower()
                desc = str(j.get('description', '')).lower()
                category = str(j.get('category', '')).lower()
                
                if kw_lower in title or kw_lower in desc or kw_lower in category:
                    filtered.append(j)
            jobs = filtered
        
        result = []
        for j in jobs[:100]:
            result.append({
                'title': j.get('title', 'Unknown'),
                'company': j.get('company_name', 'Unknown'),
                'location': 'Remote',
                'url': j.get('url', ''),
                'description': j.get('description', ''),
                'tags': [j.get('category', '')],
                'source': 'Remotive'
            })
        
        return result
    except Exception as e:
        print(f"   ⚠️  Remotive error: {e}")
        return []


def fetch_arbeitnow_jobs(keywords=None):
    """Fetch jobs from Arbeitnow API (free, no auth needed)."""
    try:
        url = "https://www.arbeitnow.com/api/job-board-api"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = httpx.get(url, headers=headers, timeout=30)
        data = response.json()
        jobs = data.get('data', [])
        
        # Filter by keywords
        if keywords:
            kw_lower = keywords.lower()
            filtered = []
            for j in jobs:
                title = str(j.get('title', '')).lower()
                desc = str(j.get('description', '')).lower()
                tags = ' '.join(str(t) for t in j.get('tags', [])).lower()
                
                if kw_lower in title or kw_lower in desc or kw_lower in tags:
                    filtered.append(j)
            jobs = filtered
        
        result = []
        for j in jobs[:100]:
            result.append({
                'title': j.get('title', 'Unknown'),
                'company': j.get('company_name', 'Unknown'),
                'location': j.get('location', 'Remote'),
                'url': j.get('url', ''),
                'description': j.get('description', ''),
                'tags': j.get('tags', []),
                'source': 'Arbeitnow'
            })
        
        return result
    except Exception as e:
        print(f"   ⚠️  Arbeitnow error: {e}")
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
    title_lower = job['title'].lower()
    
    matches = 0
    matched_skills = []
    
    for skill in user_skills:
        if skill.lower() in job_text:
            matches += 1
            matched_skills.append(skill)
    
    # Base score from skill matches
    if user_skills:
        score = int((matches / len(user_skills)) * 100)
    else:
        score = 50
    
    # Boost for role-specific keywords
    role_boosts = {
        'qa': ['qa', 'quality', 'test', 'testing', 'automation', 'selenium', 'cypress'],
        'sdet': ['sdet', 'test', 'automation', 'framework', 'ci/cd', 'jenkins'],
        'engineer': ['engineer', 'software', 'developer', 'development'],
        'senior': ['senior', 'lead', 'staff', 'principal'],
        'backend': ['backend', 'api', 'server', 'database', 'microservices'],
        'frontend': ['frontend', 'react', 'vue', 'angular', 'ui', 'ux'],
        'fullstack': ['fullstack', 'full-stack', 'full stack'],
        'devops': ['devops', 'kubernetes', 'docker', 'aws', 'cloud', 'infrastructure']
    }
    
    # Check which role categories match
    for role, keywords in role_boosts.items():
        if any(kw in title_lower for kw in keywords):
            score = min(100, score + 15)
            break
    
    # Boost for seniority match
    if any(word in title_lower for word in ['senior', 'lead', 'staff', 'principal']):
        score = min(100, score + 10)
    
    # Penalty for mismatched roles (e.g., if user is QA but job is ML Engineer)
    mismatch_keywords = {
        'machine learning': ['machine learning', 'ml engineer', 'data scientist'],
        'sales': ['sales', 'account executive', 'business development'],
        'marketing': ['marketing', 'growth', 'seo', 'content'],
        'design': ['designer', 'ux designer', 'ui designer', 'graphic']
    }
    
    for category, keywords in mismatch_keywords.items():
        if any(kw in title_lower for kw in keywords):
            # Check if user has related skills
            if not any(kw in ' '.join(user_skills).lower() for kw in keywords):
                score = max(0, score - 20)
    
    return score, len(matched_skills)


def search_and_match_jobs(keywords, career_dir, min_score=40):
    """Search jobs and match to user profile."""
    print("\n🔍 Fetching jobs from free APIs...")
    print("   • RemoteOK (remote jobs)")
    print("   • Remotive (remote jobs)")
    print("   • Arbeitnow (EU + remote jobs)")
    
    # Fetch ALL jobs first (don't filter by keywords yet)
    # We'll match them against user profile instead
    all_jobs = []
    
    # Use broad terms to get more jobs
    broad_terms = ['engineer', 'developer', 'software']
    for term in broad_terms:
        all_jobs.extend(fetch_remoteok_jobs(term))
        all_jobs.extend(fetch_remotive_jobs(term))
        all_jobs.extend(fetch_arbeitnow_jobs(term))
    
    # Remove duplicates based on URL
    seen_urls = set()
    unique_jobs = []
    for job in all_jobs:
        if job['url'] and job['url'] not in seen_urls:
            seen_urls.add(job['url'])
            unique_jobs.append(job)
    
    all_jobs = unique_jobs
    
    print(f"\n✅ Found {len(all_jobs)} jobs")
    
    if not all_jobs:
        print("\n⚠️  No jobs found. APIs may be rate-limited.")
        print("   Try again in a few minutes.")
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


def generate_linkedin_contact_url(company, role):
    """Generate LinkedIn search URL to find employees at company."""
    from urllib.parse import quote
    
    # Clean company name
    company_clean = company.replace('Inc.', '').replace('LLC', '').strip()
    
    # Generate search query
    query = f"{role} {company_clean}"
    query_encoded = quote(query)
    
    # LinkedIn people search URL
    url = f"https://www.linkedin.com/search/results/people/?keywords={query_encoded}&origin=GLOBAL_SEARCH_HEADER"
    
    return url


def save_matches_to_csv(jobs, output_file):
    """Save matched jobs to CSV with LinkedIn contact links."""
    import csv
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Match %', 'Title', 'Company', 'Location', 
            'Apply URL', 'LinkedIn Contacts', 
            'Applied', 'Status', 'Notes'
        ])
        
        for job in jobs:
            # Generate LinkedIn contact search URL
            linkedin_url = generate_linkedin_contact_url(job['company'], job['title'])
            
            writer.writerow([
                f"{job['match_score']}%",
                job['title'],
                job['company'],
                job['location'],
                job['url'],
                linkedin_url,
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
