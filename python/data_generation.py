"""
Multilingual Customer Support Analytics - Data Generation Script
Author: Ake Marc Albert Adje
Description: Generates synthetic customer support ticket data for analysis
"""

import csv
import random

# Language distribution based on European multilingual markets
LANGUAGES = {
    'en': 0.42,  # English - 42%
    'es': 0.18,  # Spanish - 18%
    'fr': 0.15,  # French - 15%
    'de': 0.12,  # German - 12%
    'pt': 0.10,  # Portuguese - 10%
    'it': 0.03   # Italian - 3%
}

REGIONS = {'Europe': 0.97, 'Americas': 0.03}
ISSUE_TYPES = {'Software': 0.67, 'Other': 0.33}
PRIORITIES = {1: 0.60, 2: 0.40}

SUBJECTS = [
    "Password Reset", "Software Install", "VPN Access", "Email Setup",
    "Account Access", "System Error", "Network Issue", "Hardware Problem",
    "Billing Question", "General Query", "License Activation", "Data Recovery",
    "Performance Issue", "Security Concern", "Integration Problem", "Update Request"
]

def generate_ticket_data(num_tickets=210):
    """
    Generate synthetic customer support ticket data
    
    Args:
        num_tickets (int): Number of tickets to generate
        
    Returns:
        list: List of ticket dictionaries
    """
    tickets = []
    random.seed(42)  # Reproducible results
    
    for ticket_id in range(1, num_tickets + 1):
        # Customer language (weighted random)
        customer_lang = random.choices(
            list(LANGUAGES.keys()), 
            weights=list(LANGUAGES.values())
        )[0]
        
        # Agent languages (2-3 random languages)
        agent_langs = random.sample(list(LANGUAGES.keys()), k=random.randint(2, 3))
        agent_langs_str = ';'.join(agent_langs)
        
        # Language match (key business metric)
        language_match = customer_lang in agent_langs
        
        # Satisfaction & resolution time (correlated with language match)
        if language_match:
            satisfaction = round(random.uniform(4.0, 5.0), 1)
            resolution_time = round(random.uniform(60, 100), 1)
        else:
            satisfaction = round(random.uniform(2.5, 4.0), 1)
            resolution_time = round(random.uniform(95, 130), 1)
        
        # Other attributes
        region = random.choices(list(REGIONS.keys()), weights=list(REGIONS.values()))[0]
        issue_type = random.choices(list(ISSUE_TYPES.keys()), weights=list(ISSUE_TYPES.values()))[0]
        priority = random.choices(list(PRIORITIES.keys()), weights=list(PRIORITIES.values()))[0]
        
        category = "Employee Inquiries-IT Support" if issue_type == "Software" else "Other"
        subject = random.choice(SUBJECTS)
        
        ticket = {
            'Ticket_id': f'T{ticket_id:03d}',
            'Customer_Language': customer_lang,
            'Agent_languages': agent_langs_str,
            'Satisfaction': satisfaction,
            'Resolution_Time': resolution_time,
            'Category_Issue': category,
            'Issue_Type': issue_type,
            'Region': region,
            'Priority': priority,
            'Language_Match': language_match,
            'Subject': subject,
            'Description': f'Support ticket for {subject.lower()}'
        }
        
        tickets.append(ticket)
    
    return tickets

def save_to_csv(tickets, filename='../data/raw/multilingual_support_tickets.csv'):
    """Save ticket data to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=tickets[0].keys())
        writer.writeheader()
        writer.writerows(tickets)
    
    print(f"✅ Generated {len(tickets)} tickets")
    print(f"✅ Saved to: {filename}")

def print_statistics(tickets):
    """Print dataset statistics"""
    matched = [t for t in tickets if t['Language_Match']]
    unmatched = [t for t in tickets if not t['Language_Match']]
    
    avg_resolution_matched = sum(t['Resolution_Time'] for t in matched) / len(matched)
    avg_resolution_unmatched = sum(t['Resolution_Time'] for t in unmatched) / len(unmatched)
    
    avg_satisfaction_matched = sum(t['Satisfaction'] for t in matched) / len(matched)
    avg_satisfaction_unmatched = sum(t['Satisfaction'] for t in unmatched) / len(unmatched)
    
    print(f"\n📊 DATASET STATISTICS:")
    print(f"   Matched tickets: {len(matched)} ({len(matched)/len(tickets)*100:.1f}%)")
    print(f"   Unmatched tickets: {len(unmatched)} ({len(unmatched)/len(tickets)*100:.1f}%)")
    print(f"\n🔍 LANGUAGE MATCH IMPACT:")
    print(f"   Resolution Time: {avg_resolution_matched:.1f}h vs {avg_resolution_unmatched:.1f}h")
    print(f"   Satisfaction: {avg_satisfaction_matched:.2f} vs {avg_satisfaction_unmatched:.2f}")

if __name__ == "__main__":
    # Generate data
    tickets = generate_ticket_data(210)
    
    # Save to CSV
    save_to_csv(tickets)
    
    # Print statistics
    print_statistics(tickets)