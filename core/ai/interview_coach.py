"""AI Interview Coach - Match explanation and interview prep"""
import os
from datetime import datetime, timedelta
import json
from pathlib import Path


def generate_match_explanation(job, user_profile, match_score):
    """
    Generate AI explanation of why user matches the job
    
    Args:
        job: Dict with title, company, description, url
        user_profile: Dict with work history, skills
        match_score: Int (0-100)
    
    Returns:
        Dict with explanation, prep plan, timeline
    """
    
    # TODO: Replace with actual OpenAI/Claude API call
    # For now, template-based
    
    explanation = {
        'job_title': job['title'],
        'company': job['company'],
        'match_score': match_score,
        'generated_at': datetime.now().isoformat(),
        
        'why_you_match': [
            {
                'reason': f"Your experience in {extract_domain(user_profile)} aligns with their requirements",
                'evidence': extract_relevant_experience(user_profile, job),
                'strength': 'high'
            },
            {
                'reason': f"Your technical skills match their stack",
                'evidence': extract_matching_skills(user_profile, job),
                'strength': 'medium'
            },
            {
                'reason': f"Your seniority level fits the role",
                'evidence': f"{user_profile.get('years_experience', 0)} years experience",
                'strength': 'high'
            }
        ],
        
        'what_to_emphasize': [
            "Lead with your most relevant project/achievement",
            "Highlight quantified results (metrics, impact)",
            "Mention specific technologies they use"
        ],
        
        'potential_gaps': [
            {
                'gap': "Skill X mentioned in job description",
                'how_to_address': "Frame as: 'Quick learner, picked up similar tech in past'"
            }
        ],
        
        'interview_prep_plan': generate_prep_plan(job, user_profile),
        
        'action_steps': [
            {
                'step': 1,
                'action': 'Find 2-3 employees on LinkedIn',
                'deadline': 'Today',
                'status': 'pending'
            },
            {
                'step': 2,
                'action': 'Prepare STAR stories for top 3 skills',
                'deadline': 'Day 2',
                'status': 'pending'
            },
            {
                'step': 3,
                'action': 'Research company recent news/products',
                'deadline': 'Day 3',
                'status': 'pending'
            }
        ]
    }
    
    return explanation


def generate_prep_plan(job, user_profile):
    """Generate week-by-week interview preparation plan"""
    
    plan = {
        'total_duration': '2 weeks',
        'weekly_breakdown': [
            {
                'week': 1,
                'focus': 'Application & Initial Prep',
                'tasks': [
                    {
                        'day': 1,
                        'task': 'Apply to job + find referrals',
                        'time': '2 hours',
                        'checklist': [
                            'Tailor resume for this role',
                            'Find 3 employees on LinkedIn',
                            'Send connection requests with note',
                            'Apply on company website'
                        ]
                    },
                    {
                        'day': 2,
                        'task': 'Prepare STAR stories',
                        'time': '3 hours',
                        'checklist': [
                            'List 5 major achievements',
                            'Write STAR format for each',
                            'Practice saying them out loud',
                            'Get feedback from friend'
                        ]
                    },
                    {
                        'day': 3,
                        'task': 'Company research',
                        'time': '2 hours',
                        'checklist': [
                            'Read company blog/news (last 6 months)',
                            'Understand their products',
                            'Note recent launches/challenges',
                            'Prepare 3 questions to ask'
                        ]
                    },
                    {
                        'day': 4,
                        'task': 'Technical review',
                        'time': '3 hours',
                        'checklist': [
                            'Review key technologies in job description',
                            'Brush up on concepts you haven\'t used recently',
                            'Prepare examples of using each tech',
                            'Practice explaining technical decisions'
                        ]
                    },
                    {
                        'day': 5,
                        'task': 'Mock interview (behavioral)',
                        'time': '2 hours',
                        'checklist': [
                            'Practice with friend/family',
                            'Record yourself answering questions',
                            'Review and improve weak answers',
                            'Time your responses (2-3 mins each)'
                        ]
                    }
                ]
            },
            {
                'week': 2,
                'focus': 'Interview Ready',
                'tasks': [
                    {
                        'day': 8,
                        'task': 'Follow up on application',
                        'time': '1 hour',
                        'checklist': [
                            'Check if referral contacts responded',
                            'Send polite follow-up if needed',
                            'Check application status',
                            'Prepare for recruiter call'
                        ]
                    },
                    {
                        'day': 9,
                        'task': 'Technical deep dive',
                        'time': '3 hours',
                        'checklist': [
                            'Review system design concepts',
                            'Practice coding/testing scenarios',
                            'Prepare for technical questions',
                            'Review your past projects in detail'
                        ]
                    },
                    {
                        'day': 10,
                        'task': 'Mock interview (technical)',
                        'time': '2 hours',
                        'checklist': [
                            'Practice technical questions',
                            'Explain your thought process',
                            'Practice whiteboarding/screen sharing',
                            'Get feedback on communication'
                        ]
                    },
                    {
                        'day': 11,
                        'task': 'Final prep',
                        'time': '2 hours',
                        'checklist': [
                            'Review all STAR stories',
                            'Review company research notes',
                            'Prepare questions to ask interviewer',
                            'Plan outfit, test video setup'
                        ]
                    },
                    {
                        'day': 12,
                        'task': 'Rest & confidence',
                        'time': '1 hour',
                        'checklist': [
                            'Light review only',
                            'Get good sleep',
                            'Prepare materials (resume, notepad)',
                            'Visualize success'
                        ]
                    }
                ]
            }
        ],
        
        'key_topics_to_prepare': extract_key_topics(job),
        
        'common_questions': [
            "Tell me about yourself",
            "Why do you want to work here?",
            "Tell me about a challenging project",
            "How do you handle conflicts?",
            "Where do you see yourself in 5 years?"
        ],
        
        'technical_topics': extract_technical_topics(job)
    }
    
    return plan


def create_checkin_schedule(prep_plan):
    """Create periodic check-in reminders"""
    
    checkins = []
    start_date = datetime.now()
    
    # Day 3 check-in
    checkins.append({
        'day': 3,
        'date': (start_date + timedelta(days=3)).strftime('%Y-%m-%d'),
        'message': "How's your prep going? Have you:\n- Applied to the job?\n- Found referral contacts?\n- Started STAR stories?",
        'tasks_to_check': ['apply', 'referrals', 'star_stories']
    })
    
    # Day 7 check-in
    checkins.append({
        'day': 7,
        'date': (start_date + timedelta(days=7)).strftime('%Y-%m-%d'),
        'message': "Week 1 complete! Have you:\n- Completed company research?\n- Practiced STAR stories?\n- Done mock interview?",
        'tasks_to_check': ['research', 'star_practice', 'mock_interview']
    })
    
    # Day 11 check-in
    checkins.append({
        'day': 11,
        'date': (start_date + timedelta(days=11)).strftime('%Y-%m-%d'),
        'message': "Almost ready! Final prep:\n- Review all materials\n- Test video setup\n- Get good rest",
        'tasks_to_check': ['final_review', 'tech_setup', 'rest']
    })
    
    return checkins


def save_prep_plan(job, explanation, prep_plan, output_dir):
    """Save complete prep plan to file"""
    
    output_path = Path(output_dir) / f"interview_prep_{job['company'].replace(' ', '_')}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    data = {
        'job': job,
        'explanation': explanation,
        'prep_plan': prep_plan,
        'checkins': create_checkin_schedule(prep_plan),
        'created_at': datetime.now().isoformat(),
        'status': 'active'
    }
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    return output_path


# Helper functions

def extract_domain(user_profile):
    """Extract user's domain (e.g., fintech, e-commerce)"""
    # Simple extraction from work history
    history = user_profile.get('manual_history', [])
    if history:
        # Look for keywords in responsibilities
        for company in history:
            resp = ' '.join(company.get('responsibilities', []))
            if 'payment' in resp.lower() or 'fintech' in resp.lower():
                return 'fintech/payments'
            if 'ecommerce' in resp.lower() or 'retail' in resp.lower():
                return 'e-commerce'
    return 'software development'


def extract_relevant_experience(user_profile, job):
    """Extract most relevant experience for this job"""
    # Simplified - would use AI in production
    history = user_profile.get('manual_history', [])
    if history:
        latest = history[0]
        return f"{latest['role']} at {latest['company']}"
    return "Your recent experience"


def extract_matching_skills(user_profile, job):
    """Find skills that match between user and job"""
    # Simplified - would use AI in production
    return "Java, Selenium, CI/CD, AWS"


def extract_key_topics(job):
    """Extract key topics to prepare from job description"""
    # Simplified - would use AI in production
    return [
        "System design and architecture",
        "Testing strategies and frameworks",
        "CI/CD and automation",
        "Team collaboration and leadership"
    ]


def extract_technical_topics(job):
    """Extract technical topics from job description"""
    # Simplified - would use AI in production
    return [
        "Automation frameworks (Selenium, TestNG)",
        "API testing (REST, GraphQL)",
        "Cloud platforms (AWS, Azure)",
        "Programming (Java, Python)"
    ]
