# Quick Start Guide

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/JobForge.git
cd JobForge

# Install dependencies
pip install -r requirements.txt
python -m playwright install chromium

# Optional: Install Bun for resume generation
curl -fsSL https://bun.sh/install | bash
```

## Setup Your Profile

1. **Add Career History**

Create files in `career/` directory:

```bash
# career/2024.md
## Senior Engineer at TechCorp (2024 - Present)
- Built ML systems with Python and TensorFlow
- Deployed on AWS with Docker and Kubernetes
**Skills**: Python, AWS, Docker, Kubernetes, TensorFlow
```

2. **Configure Preferences**

Edit `config/settings.yaml`:

```yaml
job_titles:
  - Machine Learning Engineer
  - Senior Software Engineer

locations:
  - California
  - Remote
```

## Run JobForge

```bash
# Step 1: Discover jobs
python jobforge.py discover

# Step 2: Match jobs to your profile
python jobforge.py match

# Step 3: View top matches
python jobforge.py show --top 20

# Step 4: Generate tailored resumes
python jobforge.py forge --top 10

# Step 5: Export results
python jobforge.py export --output my-jobs.csv
```

## Example Workflow

```bash
# Weekly job search
python jobforge.py discover
python jobforge.py match --min-score 70
python jobforge.py show --top 10

# Generate resumes for top 5
python jobforge.py forge --top 5 --min-score 80

# Check results
ls results/resumes/
```

## Tips

- **Update career history** monthly to keep profile current
- **Run discovery weekly** to catch new postings
- **Set min-score to 70+** for quality matches
- **Review generated resumes** before applying
- **Track applications** in a spreadsheet

## Troubleshooting

**No jobs found?**
- Check `config/companies.yaml` is configured
- Verify internet connection
- Some sites may block automated access

**Low match scores?**
- Add more skills to career files
- Use industry-standard terminology
- Include relevant technologies

**Resume generation fails?**
- Ensure Bun is installed
- Check LLM API key is set
- Try `--paste` mode for manual generation

## Next Steps

- Read full [README.md](README.md)
- Check [INTEGRATION_PLAN.md](INTEGRATION_PLAN.md) for advanced features
- Contribute at [GitHub](https://github.com/yourusername/JobForge)
