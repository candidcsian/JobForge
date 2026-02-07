"""Generate personalized referral request messages."""


def generate_connection_request(name, company, role):
    """Generate LinkedIn connection request message."""
    return f"""Hi {name},

I saw you work at {company}. I'm interested in the {role} position and would love to learn more about your experience there. Would you be open to a quick chat?

Best regards"""


def generate_referral_request(name, company, role, background):
    """Generate referral request message after connecting."""
    return f"""Hi {name},

Thanks for connecting! I've applied to the {role} position at {company}.

{background}

Would you be comfortable referring me? Happy to share more details about my background and why I'm excited about this role.

Best regards"""


def generate_follow_up(name, days=3):
    """Generate follow-up message."""
    return f"""Hi {name},

Just wanted to follow up on my previous message. I understand you're busy, but I'd really appreciate any insights you could share about working at your company.

Thanks!"""


# Message templates
TEMPLATES = {
    'connection_request': """Hi {name},

I saw you work at {company}. I'm interested in the {role} position and would love to learn more about your experience there. Would you be open to a quick chat?""",
    
    'referral_request': """Hi {name},

Thanks for connecting! I've applied to the {role} position at {company}.

Quick background: {background}

Would you be comfortable referring me? Happy to share my resume and discuss why I'm excited about this opportunity.

Best regards""",
    
    'follow_up': """Hi {name},

Following up on my previous message about the {role} position. I understand you're busy, but would really appreciate any insights about the role or team.

Thanks!""",
    
    'thank_you': """Hi {name},

Thank you so much for the referral! I really appreciate you taking the time to help. I'll keep you posted on how it goes.

Best regards"""
}


def format_message(template_name, **kwargs):
    """Format a message template with provided values."""
    template = TEMPLATES.get(template_name, '')
    return template.format(**kwargs)


if __name__ == '__main__':
    # Example usage
    print("Connection Request:")
    print(format_message('connection_request', 
                        name='John',
                        company='OpenAI',
                        role='ML Engineer'))
    
    print("\n" + "="*50 + "\n")
    
    print("Referral Request:")
    print(format_message('referral_request',
                        name='John',
                        company='OpenAI',
                        role='ML Engineer',
                        background='5+ years in ML, built recommendation systems at scale'))
