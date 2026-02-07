"""Discovery orchestrator - coordinates job search across companies."""
import sys
import yaml
from pathlib import Path
from datetime import datetime

# Import Argus components
try:
    from core.discovery.models import Company, Job
    from core.discovery.registry import CompanyRegistry
    from core.discovery.filter import JobFilter
    from core.discovery.store import JobStore
    from core.discovery.ats import (
        ATSDetector,
        GreenhouseFetcher,
        LeverFetcher,
        AshbyFetcher,
        WorkdayFetcher,
        GenericFetcher,
        UberFetcher,
        AmazonFetcher,
        MetaFetcher,
        GoogleFetcher,
        TikTokFetcher,
    )
    ARGUS_AVAILABLE = True
except ImportError as e:
    ARGUS_AVAILABLE = False
    IMPORT_ERROR = str(e)


def run_discovery(args):
    """Run job discovery."""
    print("🔍 JobForge - Job Discovery")
    print("="*50)
    
    if not ARGUS_AVAILABLE:
        print(f"\n⚠️  Discovery module error: {IMPORT_ERROR}")
        print("\nInstall dependencies:")
        print("  pip install playwright httpx pyyaml")
        print("  python -m playwright install chromium")
        return 1
    
    # Load companies config
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"\n❌ Config not found: {config_path}")
        return 1
    
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    companies = config.get('companies', [])
    
    # Filter companies if specified
    if args.companies:
        company_names = [c.strip() for c in args.companies.split(',')]
        companies = [c for c in companies if c['name'] in company_names]
    
    print(f"\n📋 Searching {len(companies)} companies")
    print(f"⏱️  Timeout: {args.timeout}s")
    print("="*50)
    
    # Initialize components
    output_dir = Path('results/jobs') / datetime.now().strftime('%Y-%m-%d')
    store = JobStore(str(output_dir))
    
    total_jobs = 0
    successful = 0
    
    for i, company_config in enumerate(companies, 1):
        company_name = company_config['name']
        career_url = company_config['career_url']
        ats_type = company_config.get('ats_type', 'generic')
        
        print(f"\n[{i}/{len(companies)}] {company_name}")
        print(f"   URL: {career_url}")
        print(f"   ATS: {ats_type}")
        
        try:
            # Select fetcher based on ATS type
            fetcher = get_fetcher(ats_type, career_url, args.timeout)
            
            # Fetch jobs
            jobs = fetcher.fetch_job_list()
            
            if jobs:
                # Save jobs
                company = Company(name=company_name, career_url=career_url)
                store.save_jobs(company, jobs)
                
                print(f"   ✅ Found {len(jobs)} jobs")
                total_jobs += len(jobs)
                successful += 1
            else:
                print(f"   ⚠️  No jobs found")
                
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
    
    print("\n" + "="*50)
    print(f"✅ Discovery Complete!")
    print(f"   Companies searched: {successful}/{len(companies)}")
    print(f"   Total jobs found: {total_jobs}")
    print(f"   Saved to: {output_dir}")
    
    return 0


def get_fetcher(ats_type, url, timeout):
    """Get appropriate fetcher for ATS type."""
    # Extract company name from URL
    from urllib.parse import urlparse
    parsed = urlparse(url)
    company_name = parsed.path.strip('/').split('/')[0] if parsed.path else 'Unknown'
    
    fetchers = {
        'greenhouse': GreenhouseFetcher,
        'lever': LeverFetcher,
        'ashby': AshbyFetcher,
        'workday': WorkdayFetcher,
        'uber': UberFetcher,
        'amazon': AmazonFetcher,
        'meta': MetaFetcher,
        'google': GoogleFetcher,
        'tiktok': TikTokFetcher,
    }
    
    fetcher_class = fetchers.get(ats_type, GenericFetcher)
    return fetcher_class(company_name, url, timeout=timeout)
