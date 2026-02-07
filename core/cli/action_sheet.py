"""Generate action sheet CSV with all information needed for applications."""
import json
import csv
from pathlib import Path
from datetime import datetime


def generate_action_sheet():
    """Generate comprehensive action sheet for job applications."""
    
    # Load scored jobs
    matches_dir = Path('results/matches')
    date_dirs = sorted([d for d in matches_dir.iterdir() if d.is_dir()], reverse=True)
    
    if not date_dirs:
        print("❌ No match results found. Run matching first.")
        return
    
    latest = date_dirs[0]
    
    # Load scored jobs
    with open(latest / 'scored_jobs.json') as f:
        jobs = json.load(f)
    
    # Load employee search results
    employee_file = latest / 'employee_search.json'
    employees = {}
    if employee_file.exists():
        with open(employee_file) as f:
            emp_data = json.load(f)
            for item in emp_data:
                employees[item['company']] = item
    
    # Generate action sheet
    output_file = latest / 'ACTION_SHEET.csv'
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Priority',
            'Score',
            'Company',
            'Job Title',
            'Location',
            'Job URL',
            'Resume File',
            'LinkedIn - Find Employees',
            'LinkedIn - Find Engineers',
            'LinkedIn - Find Recruiters',
            'Status',
            'Referral Contact',
            'Applied Date',
            'Notes'
        ])
        
        # Data rows
        for i, job in enumerate(jobs, 1):
            company = job.get('company', '')
            emp_info = employees.get(company, {})
            
            resume_file = f"results/resumes/{company.lower().replace(' ', '-')}-{job.get('title', '').lower().replace(' ', '-')[:30]}.md"
            
            writer.writerow([
                i,  # Priority
                f"{job.get('score', 0)}%",
                company,
                job.get('title', ''),
                job.get('location', ''),
                job.get('url', ''),
                resume_file,
                emp_info.get('linkedin_all', ''),
                emp_info.get('linkedin_engineers', ''),
                emp_info.get('linkedin_recruiters', ''),
                'TODO',  # Status
                '',  # Referral Contact (user fills)
                '',  # Applied Date (user fills)
                ''   # Notes (user fills)
            ])
    
    print(f"\n✅ Action sheet created: {output_file}")
    print("\n📋 Columns:")
    print("   1. Priority - Ranked by match score")
    print("   2. Score - How well job matches your profile")
    print("   3. Company - Company name")
    print("   4. Job Title - Position title")
    print("   5. Location - Job location")
    print("   6. Job URL - Direct link to apply")
    print("   7. Resume File - Which tailored resume to use")
    print("   8-10. LinkedIn Links - Find employees/engineers/recruiters")
    print("   11. Status - Track progress (TODO/CONTACTED/APPLIED/INTERVIEW)")
    print("   12. Referral Contact - Name of person who referred you")
    print("   13. Applied Date - When you applied")
    print("   14. Notes - Any additional notes")
    
    print("\n💡 How to use:")
    print("   1. Open in Excel/Google Sheets")
    print("   2. Click LinkedIn links to find employees")
    print("   3. Update Status as you progress")
    print("   4. Track referrals and applications")
    
    return output_file


if __name__ == '__main__':
    generate_action_sheet()
