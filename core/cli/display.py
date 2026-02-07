"""Display utilities for showing match results."""
import json
from pathlib import Path


def show_matches(args):
    """Display match results."""
    print("📊 JobForge - Match Results")
    print("="*70)
    
    # Load latest results
    matches_dir = Path('results/matches')
    if not matches_dir.exists():
        print("\n❌ No results found. Run matching first:")
        print("   python jobforge.py match")
        return 1
    
    date_dirs = sorted([d for d in matches_dir.iterdir() if d.is_dir()], reverse=True)
    if not date_dirs:
        print("\n❌ No match results found.")
        return 1
    
    latest = date_dirs[0]
    json_file = latest / 'scored_jobs.json'
    
    with open(json_file) as f:
        jobs = json.load(f)
    
    # Filter
    if args.company:
        jobs = [j for j in jobs if args.company.lower() in j.get('company', '').lower()]
    
    if args.min_score:
        jobs = [j for j in jobs if j['score'] >= args.min_score]
    
    # Show top N
    display_jobs = jobs[:args.top]
    
    print(f"\nShowing top {len(display_jobs)} of {len(jobs)} matches")
    print("="*70)
    
    for i, job in enumerate(display_jobs, 1):
        stars = "⭐⭐⭐" if job['score'] >= 80 else "⭐⭐" if job['score'] >= 60 else "⭐"
        
        print(f"\n{i}. {job.get('company', 'Unknown')} - {job.get('title', 'Unknown')}")
        print(f"   Score: {job['score']}% {stars}")
        print(f"   Location: {job.get('location', 'N/A')}")
        
        if job.get('matched_skills'):
            print(f"   Skills: {', '.join(job['matched_skills'][:5])}")
        
        print(f"   URL: {job.get('url', 'N/A')}")
    
    return 0
