# How to Add More Companies to JobForge

## Quick Method

Edit `~/JobForge/config/companies.yaml`:

```bash
vim ~/JobForge/config/companies.yaml
# or
nano ~/JobForge/config/companies.yaml
```

Add your company at the end:

```yaml
- name: Your Company Name
  career_url: https://company.com/careers
  ats_type: greenhouse  # or lever, ashby, workday, etc.
```

## Step-by-Step Guide

### 1. Find the Company's Career Page

Visit the company website and find their careers/jobs page.

**Examples:**
- Notion: https://www.notion.so/careers
- Figma: https://www.figma.com/careers
- Discord: https://discord.com/careers

### 2. Identify the ATS Type

Look at the URL or page structure:

**Greenhouse** (most common for startups)
- URL contains: `boards.greenhouse.io/companyname`
- Example: `https://boards.greenhouse.io/notion`

**Lever**
- URL contains: `jobs.lever.co/companyname`
- Example: `https://jobs.lever.co/figma`

**Ashby**
- URL contains: `jobs.ashbyhq.com/companyname`
- Example: `https://jobs.ashbyhq.com/notion`

**Workday** (common for large companies)
- URL contains: `myworkdayjobs.com`
- Example: Microsoft, Apple, Netflix

**Custom**
- Company's own career site
- Use `custom` or `generic` as ats_type

### 3. Add to Config File

Open the file:
```bash
cd ~/JobForge
vim config/companies.yaml
```

Add at the end (keep the format):
```yaml
- name: Notion
  career_url: https://boards.greenhouse.io/notion
  ats_type: greenhouse

- name: Figma
  career_url: https://jobs.lever.co/figma
  ats_type: lever

- name: Discord
  career_url: https://discord.com/careers
  ats_type: custom
```

### 4. Test It

```bash
cd ~/JobForge
source venv/bin/activate

# Test with just your new company
python3 jobforge.py discover --companies "Notion"
```

## Common ATS Types

| ATS Type | Used By | URL Pattern |
|----------|---------|-------------|
| `greenhouse` | Most startups | boards.greenhouse.io/company |
| `lever` | Figma, Spotify, Palantir | jobs.lever.co/company |
| `ashby` | OpenAI, Scale AI | jobs.ashbyhq.com/company |
| `workday` | Microsoft, Apple | myworkdayjobs.com |
| `custom` | Company-specific | Various |
| `generic` | Fallback | Any |

## Examples to Add

### Add Notion
```yaml
- name: Notion
  career_url: https://boards.greenhouse.io/notion
  ats_type: greenhouse
```

### Add Figma
```yaml
- name: Figma
  career_url: https://jobs.lever.co/figma
  ats_type: lever
```

### Add Canva
```yaml
- name: Canva
  career_url: https://www.canva.com/careers/jobs/
  ats_type: custom
```

### Add Shopify
```yaml
- name: Shopify
  career_url: https://www.shopify.com/careers
  ats_type: custom
```

### Add GitLab
```yaml
- name: GitLab
  career_url: https://boards.greenhouse.io/gitlab
  ats_type: greenhouse
```

## Quick Add Script

Or use this one-liner to add a company:

```bash
cd ~/JobForge

# Add Notion
cat >> config/companies.yaml << 'EOF'
- name: Notion
  career_url: https://boards.greenhouse.io/notion
  ats_type: greenhouse
EOF

# Test it
source venv/bin/activate
python3 jobforge.py discover --companies "Notion"
```

## Tips

1. **Start with Greenhouse** - Most startups use it
2. **Check the URL** - Usually reveals the ATS type
3. **Test individually** - Use `--companies "CompanyName"` to test
4. **Use generic fallback** - If unsure, use `ats_type: generic`

## Verify Your Addition

```bash
# Count companies
grep "^- name:" config/companies.yaml | wc -l

# List all companies
grep "^- name:" config/companies.yaml

# Test your new company
source venv/bin/activate
python3 jobforge.py discover --companies "YourCompany"
```

## Full Example

```bash
cd ~/JobForge

# 1. Edit config
vim config/companies.yaml

# Add these lines at the end:
# - name: Notion
#   career_url: https://boards.greenhouse.io/notion
#   ats_type: greenhouse
# 
# - name: Figma
#   career_url: https://jobs.lever.co/figma
#   ats_type: lever

# 2. Save and test
source venv/bin/activate
python3 jobforge.py discover --companies "Notion,Figma"

# 3. If successful, run full discovery
python3 jobforge.py discover
```

---

**Now you can add any company you want to search!** 🔨
