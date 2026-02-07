"""Search job aggregators for broader coverage."""
import httpx
from urllib.parse import quote
from pathlib import Path
import json
from datetime import datetime


def search_linkedin_jobs(keywords, location, limit=100):
    """Generate LinkedIn Jobs search URL."""
    keywords_encoded = quote(keywords)
    location_encoded = quote(location)
    
    url = f"https://www.linkedin.com/jobs/search/?keywords={keywords_encoded}&location={location_encoded}&f_TPR=r604800"
    
    return {
        'source': 'LinkedIn Jobs',
        'url': url,
        'instructions': 'Open this URL in browser to see all matching jobs'
    }


def search_indeed(keywords, location):
    """Generate Indeed search URL."""
    keywords_encoded = quote(keywords)
    location_encoded = quote(location)
    
    url = f"https://www.indeed.com/jobs?q={keywords_encoded}&l={location_encoded}&fromage=7"
    
    return {
        'source': 'Indeed',
        'url': url,
        'instructions': 'Open this URL in browser to see all matching jobs'
    }


def search_glassdoor(keywords, location):
    """Generate Glassdoor search URL."""
    keywords_encoded = quote(keywords)
    location_encoded = quote(location)
    
    url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={keywords_encoded}&locT=C&locId=&jobType=&fromAge=7&minSalary=0&includeNoSalaryJobs=true&radius=0&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0"
    
    return {
        'source': 'Glassdoor',
        'url': url,
        'instructions': 'Open this URL in browser to see all matching jobs'
    }


def search_wellfound(keywords, location):
    """Generate Wellfound (AngelList) search URL."""
    keywords_encoded = quote(keywords)
    
    url = f"https://wellfound.com/jobs?query={keywords_encoded}"
    
    return {
        'source': 'Wellfound (Startups)',
        'url': url,
        'instructions': 'Open this URL in browser to see startup jobs'
    }


def search_ycombinator(keywords):
    """Generate Y Combinator jobs search URL."""
    url = "https://www.ycombinator.com/jobs"
    
    return {
        'source': 'Y Combinator Jobs',
        'url': url,
        'instructions': 'Search for your role on this page'
    }


def search_all_aggregators(keywords, location):
    """Search all job aggregators."""
    print("\n🌐 JobForge - Aggregator Search")
    print("="*70)
    print(f"\n🔍 Searching for: {keywords}")
    print(f"📍 Location: {location}")
    print("="*70)
    
    aggregators = [
        search_linkedin_jobs(keywords, location),
        search_indeed(keywords, location),
        search_glassdoor(keywords, location),
        search_wellfound(keywords, location),
        search_ycombinator(keywords)
    ]
    
    print("\n📋 Job Aggregator Links:")
    print("="*70)
    
    for i, agg in enumerate(aggregators, 1):
        print(f"\n{i}. {agg['source']}")
        print(f"   🔗 {agg['url']}")
        print(f"   💡 {agg['instructions']}")
    
    # Save results
    output_dir = Path('results/aggregators')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"search-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output_file, 'w') as f:
        json.dump({
            'keywords': keywords,
            'location': location,
            'aggregators': aggregators,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)
    
    print(f"\n✅ Links saved to: {output_file}")
    
    print("\n" + "="*70)
    print("💡 TIPS FOR AGGREGATOR SEARCH")
    print("="*70)
    print("""
1. LinkedIn Jobs - Best for tech roles, shows company size
2. Indeed - Largest database, all industries
3. Glassdoor - Includes salary info and reviews
4. Wellfound - Best for startups and early-stage companies
5. Y Combinator - YC-backed startups only

FILTERS TO USE:
- Date posted: Last 7 days
- Remote: Yes (if applicable)
- Experience level: Match your background
- Company size: Startup / Mid-size / Enterprise

STRATEGY:
1. Open all 5 links in separate tabs
2. Apply filters on each site
3. Save interesting jobs
4. Use JobForge to find employees at those companies
5. Get referrals before applying
""")
    
    return aggregators


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python aggregator_search.py 'keywords' 'location'")
        print("\nExample:")
        print("  python aggregator_search.py 'Machine Learning Engineer' 'Remote'")
        print("  python aggregator_search.py 'Software Engineer' 'San Francisco'")
        sys.exit(1)
    
    keywords = sys.argv[1]
    location = sys.argv[2]
    
    search_all_aggregators(keywords, location)
