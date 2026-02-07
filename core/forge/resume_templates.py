"""Resume templates based on 29 Amazon/AWS employee resumes."""

AMAZON_STYLE_TEMPLATE = """# {name}
{contact_info}

## SUMMARY
{summary}

## EXPERIENCE

{experience}

## TECHNICAL SKILLS
{skills}

## EDUCATION
{education}
"""

def generate_amazon_style_summary(profile, job):
    """Generate Amazon-style summary with impact focus."""
    years = profile.get('years', 0)
    level = "Senior" if years >= 5 else "Experienced" if years >= 3 else ""
    
    return f"""{level} Software Engineer with {years}+ years building scalable systems. Proven track record of delivering high-impact solutions. Strong expertise in {', '.join(profile['skills'][:3])}. Seeking {job['title']} role at {job['company']}."""

def format_experience_amazon_style(career_files):
    """Format experience with Amazon's impact-focused style."""
    experiences = []
    
    for file in career_files:
        content = file.read_text()
        lines = content.split('\n')
        
        for line in lines:
            if line.startswith('##') and ' at ' in line:
                # Extract title and company
                title_line = line.replace('#', '').strip()
                experiences.append(f"\n### {title_line}")
            elif line.startswith('- '):
                # Convert to impact statement
                bullet = line[2:].strip()
                if any(word in bullet.lower() for word in ['built', 'led', 'reduced', 'improved', 'launched']):
                    experiences.append(f"- {bullet}")
    
    return '\n'.join(experiences)

def format_skills_by_category(skills):
    """Organize skills by category like Amazon resumes."""
    categories = {
        'Languages': ['python', 'java', 'javascript', 'typescript', 'go', 'rust', 'c++'],
        'Cloud & Infrastructure': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform'],
        'Databases': ['postgresql', 'mysql', 'mongodb', 'redis', 'dynamodb', 'sql'],
        'Frameworks': ['react', 'django', 'flask', 'spring', 'node', 'express'],
        'ML/AI': ['tensorflow', 'pytorch', 'machine learning', 'deep learning', 'nlp']
    }
    
    organized = {}
    for category, keywords in categories.items():
        matched = [s for s in skills if any(k in s.lower() for k in keywords)]
        if matched:
            organized[category] = matched
    
    result = []
    for category, items in organized.items():
        result.append(f"**{category}**: {', '.join(items)}")
    
    return '\n'.join(result)

def generate_tailored_resume(profile, job, career_files):
    """Generate resume tailored for specific job using Amazon patterns."""
    
    summary = generate_amazon_style_summary(profile, job)
    experience = format_experience_amazon_style(career_files)
    skills = format_skills_by_category(profile['skills'])
    
    resume = AMAZON_STYLE_TEMPLATE.format(
        name="[Your Name]",
        contact_info="**Email**: your.email@example.com | **Phone**: (555) 123-4567 | **LinkedIn**: linkedin.com/in/yourprofile",
        summary=summary,
        experience=experience,
        skills=skills,
        education="**Bachelor of Science in Computer Science**\nUniversity Name, Year"
    )
    
    # Add job-specific section
    resume += f"\n\n---\n\n## WHY {job['company'].upper()}\n"
    resume += f"Excited about {job['title']} role because:\n"
    resume += f"- Strong alignment with {', '.join(job.get('matched_skills', [])[:3])}\n"
    resume += f"- {profile['years']}+ years relevant experience\n"
    resume += f"- Proven track record in similar roles\n"
    
    return resume
