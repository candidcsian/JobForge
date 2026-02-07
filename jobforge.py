"""
JobForge - AI-Powered Job Discovery and Application Tool

Main CLI entry point for all JobForge operations.
"""
import sys
import os
import argparse
from pathlib import Path

# Set terminal title
sys.stdout.write("\033]0;Job Search\007")
sys.stdout.flush()

# Add core modules to path
sys.path.insert(0, str(Path(__file__).parent / 'core'))

from core.discovery.orchestrator import run_discovery
from core.matching.matcher import run_matching
from core.forge.generator import run_forge


def main():
    parser = argparse.ArgumentParser(
        description='JobForge - Forge your career path with AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  jobforge discover                    # Find jobs from all companies
  jobforge match                       # Score jobs against your profile
  jobforge forge --top 10              # Generate resumes for top 10 matches
  jobforge show --top 20               # View top 20 matches
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Discover command
    discover = subparsers.add_parser('discover', help='Discover jobs from company career pages')
    discover.add_argument('--companies', help='Comma-separated company names')
    discover.add_argument('--timeout', type=int, default=30, help='Request timeout (seconds)')
    discover.add_argument('--config', default='config/companies.yaml', help='Companies config file')
    
    # Match command
    match = subparsers.add_parser('match', help='Match jobs to your profile')
    match.add_argument('--resume', help='Path to resume file (PDF/DOCX/TXT)')
    match.add_argument('--career-dir', default='career', help='Career history directory')
    match.add_argument('--min-score', type=float, default=40, help='Minimum match score')
    match.add_argument('--output', default='results/matches', help='Output directory')
    
    # Forge command
    forge = subparsers.add_parser('forge', help='Generate tailored resumes')
    forge.add_argument('--top', type=int, default=5, help='Generate for top N matches')
    forge.add_argument('--min-score', type=float, default=70, help='Minimum match score')
    forge.add_argument('--type', default='software-engineer', help='Resume type')
    forge.add_argument('--output', default='results/resumes', help='Output directory')
    
    # Show command
    show = subparsers.add_parser('show', help='Show match results')
    show.add_argument('--top', type=int, default=10, help='Show top N matches')
    show.add_argument('--company', help='Filter by company name')
    show.add_argument('--min-score', type=float, help='Minimum score to show')
    
    # Export command
    export = subparsers.add_parser('export', help='Export results to CSV')
    export.add_argument('--output', default='jobforge-results.csv', help='Output CSV file')
    export.add_argument('--min-score', type=float, help='Minimum score to export')
    
    # Referral command
    referral = subparsers.add_parser('referral', help='Find employees for referrals')
    referral.add_argument('--top', type=int, default=10, help='Top N companies')
    referral.add_argument('--open', action='store_true', help='Open LinkedIn in browser')
    
    # Search command (NEW!)
    search = subparsers.add_parser('search', help='Search job aggregators (all companies)')
    search.add_argument('keywords', help='Job title/keywords (e.g. "Machine Learning Engineer")')
    search.add_argument('--location', default='Remote', help='Location (default: Remote)')
    
    # Init command
    init = subparsers.add_parser('init', help='Initialize JobForge in current directory')
    init.add_argument('--example', action='store_true', help='Create example files')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Route to appropriate handler
    if args.command == 'discover':
        run_discovery(args)
    elif args.command == 'match':
        run_matching(args)
    elif args.command == 'forge':
        run_forge(args)
    elif args.command == 'show':
        from core.cli.display import show_matches
        show_matches(args)
    elif args.command == 'export':
        from core.cli.export import export_results
        export_results(args)
    elif args.command == 'referral':
        from core.referral.finder import find_employees
        find_employees(args)
    elif args.command == 'search':
        from core.discovery.aggregator_search import search_all_aggregators
        search_all_aggregators(args.keywords, args.location)
    elif args.command == 'init':
        from core.cli.init import initialize_project
        initialize_project(args)


if __name__ == '__main__':
    main()
