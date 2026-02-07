"""Initialize JobForge project."""
from pathlib import Path
import shutil


def initialize_project(args):
    """Initialize JobForge in current directory."""
    print("🔨 Initializing JobForge")
    print("="*50)
    
    # Create directories
    dirs = [
        'career',
        'config',
        'results/jobs',
        'results/matches',
        'results/resumes',
        'templates/resume-types'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {dir_path}/")
    
    if args.example:
        # Create example files
        create_example_career()
        create_example_config()
        print("\n✅ Created example files")
    
    print("\n🎉 JobForge initialized!")
    print("\nNext steps:")
    print("  1. Edit career/*.md with your experience")
    print("  2. Edit config/settings.yaml with preferences")
    print("  3. Run: python jobforge.py discover")
    
    return 0


def create_example_career():
    """Create example career file."""
    content = """# 2024 Work Experience

## Your Title at Company Name (Start Date - Present)

### Responsibilities
- Describe your main responsibilities
- What you work on day-to-day
- Team size and collaboration

### Key Achievements
- Quantifiable achievement #1
- Quantifiable achievement #2
- Impact you made

### Technologies Used
**Languages**: Python, JavaScript, etc.
**Frameworks**: React, Django, etc.
**Cloud**: AWS, Azure, GCP
**Tools**: Docker, Kubernetes, etc.

### Projects
1. **Project Name**: Brief description and impact
2. **Another Project**: What you built and why
"""
    
    Path('career/2024.md').write_text(content)


def create_example_config():
    """Create example config."""
    content = """# JobForge Settings

job_titles:
  - Software Engineer
  - Your Target Title

locations:
  - Your City
  - Remote

exclude_levels:
  - junior
  - intern

min_match_score: 60
"""
    
    Path('config/settings.yaml').write_text(content)
