"""Resume generator - creates tailored resumes for jobs."""
import json
from pathlib import Path


def run_forge(args):
    """Generate tailored resumes."""
    print("📄 JobForge - Resume Generation")
    print("="*50)
    
    # Load scored jobs
    matches_dir = Path('results/matches')
    if not matches_dir.exists():
        print("\n❌ No matches found. Run matching first:")
        print("   python jobforge.py match")
        return 1
    
    # Find latest results
    date_dirs = sorted([d for d in matches_dir.iterdir() if d.is_dir()], reverse=True)
    if not date_dirs:
        print("\n❌ No match results found.")
        return 1
    
    latest = date_dirs[0]
    json_file = latest / 'scored_jobs.json'
    
    if not json_file.exists():
        print(f"\n❌ No scored jobs found in {latest}")
        return 1
    
    with open(json_file) as f:
        jobs = json.load(f)
    
    # Filter by score
    filtered = [j for j in jobs if j['score'] >= args.min_score]
    top_jobs = filtered[:args.top]
    
    print(f"\n📊 Loaded {len(jobs)} scored jobs")
    print(f"   Filtered to {len(filtered)} jobs >= {args.min_score}%")
    print(f"   Generating resumes for top {len(top_jobs)}")
    
    if not top_jobs:
        print(f"\n❌ No jobs found with score >= {args.min_score}")
        print("   Try lowering --min-score")
        return 1
    
    # Generate resumes
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🔨 Generating resumes...")
    print("="*70)
    
    for i, job in enumerate(top_jobs, 1):
        print(f"\n[{i}/{len(top_jobs)}] {job['company']} - {job['title']}")
        print(f"   Score: {job['score']}%")
        
        # Generate resume (placeholder)
        resume_path = output_dir / f"{job['company'].lower().replace(' ', '-')}-{job['title'].lower().replace(' ', '-')[:30]}.md"
        
        generate_resume_placeholder(job, resume_path)
        print(f"   ✅ Saved: {resume_path.name}")
    
    print(f"\n✅ Generated {len(top_jobs)} resumes")
    print(f"📂 Location: {output_dir}")
    
    print("\n💡 Next steps:")
    print("   1. Review generated resumes")
    print("   2. Customize as needed")
    print("   3. Apply to jobs!")
    
    return 0


def generate_resume_placeholder(job, output_path):
    """Generate resume using Amazon/AWS patterns."""
    from pathlib import Path
    try:
        from core.forge.resume_templates import generate_tailored_resume, format_skills_by_category
        
        # Load career files
        career_dir = Path('career')
        career_files = list(career_dir.glob('*.md'))
        
        # Build profile
        profile = {
            'skills': job.get('matched_skills', []),
            'years': 5  # Default, should come from career parsing
        }
        
        # Generate using Amazon patterns
        content = generate_tailored_resume(profile, job, career_files)
        
    except Exception as e:
        # Fallback to simple template
        content = f"""# {job['company']} - {job['title']}

**Match Score: {job['score']}%** | **Location**: {job.get('location', 'N/A')}

## SUMMARY
Experienced engineer with strong background in {', '.join(job.get('matched_skills', [])[:3])}. 
Seeking {job['title']} role at {job['company']}.

## EXPERIENCE
[Add your experience from career/*.md files]

## SKILLS
{', '.join(job.get('matched_skills', []))}

## WHY {job['company'].upper()}
- {job['score']}% match with requirements
- Strong alignment with role
- Proven track record

**Apply**: {job.get('url', 'N/A')}
"""
    
    output_path.write_text(content)
