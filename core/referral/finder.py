"""Find employees at target companies for referrals."""
import json
import sys
from pathlib import Path
from urllib.parse import quote


def find_employees(args):
    """Find employees at top matching companies."""
    print("\n🔍 JobForge - Employee Finder")
    print("="*70)
    
    # Load scored jobs
    matches_dir = Path('results/matches')
    if not matches_dir.exists():
        print("\n❌ No matches found. Run matching first.")
        return 1
    
    # Find latest results
    date_dirs = sorted([d for d in matches_dir.iterdir() if d.is_dir()], reverse=True)
    if not date_dirs:
        print("\n❌ No match results found.")
        return 1
    
    latest = date_dirs[0]
    json_file = latest / 'scored_jobs.json'
    
    with open(json_file) as f:
        jobs = json.load(f)
    
    # Get top N companies
    top_n = int(args.top) if hasattr(args, 'top') else 10
    top_jobs = jobs[:top_n]
    
    # Group by company
    companies = {}
    for job in top_jobs:
        company = job['company']
        if company not in companies:
            companies[company] = []
        companies[company].append(job)
    
    print(f"\n📋 Found {len(companies)} companies in top {top_n} matches")
    print("="*70)
    
    # Generate LinkedIn search links
    results = []
    for i, (company, company_jobs) in enumerate(companies.items(), 1):
        print(f"\n{i}. {company} ({len(company_jobs)} matching jobs)")
        
        # LinkedIn search URLs
        linkedin_search = generate_linkedin_search(company)
        
        print(f"   🔗 Find employees:")
        print(f"      {linkedin_search['all']}")
        print(f"   🔗 Find engineers:")
        print(f"      {linkedin_search['engineers']}")
        print(f"   🔗 Find recruiters:")
        print(f"      {linkedin_search['recruiters']}")
        
        # Sample jobs
        print(f"   📄 Open roles:")
        for job in company_jobs[:3]:
            print(f"      • {job['title']} ({job['score']}%)")
        
        results.append({
            'company': company,
            'jobs_count': len(company_jobs),
            'linkedin_all': linkedin_search['all'],
            'linkedin_engineers': linkedin_search['engineers'],
            'linkedin_recruiters': linkedin_search['recruiters'],
            'top_jobs': company_jobs[:3]
        })
    
    # Save results
    output_file = latest / 'employee_search.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*70)
    print("💡 REFERRAL STRATEGY")
    print("="*70)
    print("""
1. Click the LinkedIn links above
2. Look for:
   • 2nd degree connections (easier to reach)
   • People with similar background
   • Recent joiners (more likely to help)
   
3. Send connection request with note:
   "Hi [Name], I saw you work at [Company]. I'm interested in 
   the [Role] position and would love to learn more about your 
   experience there. Would you be open to a quick chat?"
   
4. After connecting, ask for referral:
   "Thanks for connecting! I've applied to the [Role] position. 
   Would you be comfortable referring me? Happy to share my 
   background. [Attach resume]"
   
5. Apply with referral code/link they provide
""")
    
    print(f"✅ Results saved to: {output_file}")
    print("\n📊 Success Rates:")
    print("   • Cold application: 2-5% response")
    print("   • With referral: 30-50% response")
    print("   • Referrals are 10-15x more effective!")
    
    return 0


def generate_linkedin_search(company):
    """Generate LinkedIn search URLs for a company."""
    company_encoded = quote(company)
    
    return {
        'all': f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%22{company_encoded}%22%5D",
        'engineers': f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%22{company_encoded}%22%5D&keywords=software%20engineer",
        'recruiters': f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%22{company_encoded}%22%5D&keywords=recruiter"
    }


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Find employees for referrals')
    parser.add_argument('--top', type=int, default=10, help='Top N companies')
    
    args = parser.parse_args()
    sys.exit(find_employees(args))
