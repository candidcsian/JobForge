"""Export utilities for results."""
import json
import csv
from pathlib import Path


def export_results(args):
    """Export results to CSV."""
    print(f"📤 Exporting results to: {args.output}")
    
    # Load latest results
    matches_dir = Path('results/matches')
    if not matches_dir.exists():
        print("\n❌ No results found.")
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
    if args.min_score:
        jobs = [j for j in jobs if j['score'] >= args.min_score]
    
    # Export
    with open(args.output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Score', 'Company', 'Title', 'Location', 'URL', 'Matched Skills'])
        writer.writeheader()
        
        for job in jobs:
            writer.writerow({
                'Score': job['score'],
                'Company': job.get('company', ''),
                'Title': job.get('title', ''),
                'Location': job.get('location', ''),
                'URL': job.get('url', ''),
                'Matched Skills': ', '.join(job.get('matched_skills', []))
            })
    
    print(f"✅ Exported {len(jobs)} jobs to {args.output}")
    return 0
