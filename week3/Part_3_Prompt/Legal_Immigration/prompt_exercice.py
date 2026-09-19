from week3.Part_3_Prompt.prompt_test import get_answer
from pathlib import Path

user_question = "Where can I get free immigration or legal help in Ottawa?"
legal_resources = [
    {
        "name": "Ottawa Newcomer Legal Clinic",
        "service": "Free legal information and immigration support",
        "address": "400 Queen Street, Ottawa, ON",
        "phone": "613-555-0108",
        "hours": "Monday–Friday, 9:00 AM–4:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Services are available to eligible newcomers.",
        "cost": "Free."
    },
    {
        "name": "Community Legal Assistance Centre",
        "service": "Legal information related to housing, employment, and family matters",
        "address": "125 Bronson Avenue, Ottawa, ON",
        "phone": "613-555-0190",
        "hours": "Monday–Friday, 9:00 AM–5:00 PM",
        "languages": ["English", "French"],
        "eligibility": "Income eligibility may apply.",
        "cost": "Free for eligible clients."
    },
    {
        "name": "Immigration Information Helpline",
        "service": "General immigration information and referrals",
        "address": "Phone service only",
        "phone": "613-555-0161",
        "hours": "Monday–Friday, 8:00 AM–6:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Open to newcomers and people seeking immigration information.",
        "cost": "Free."
    }
]
prompt = """
^ WRITE YOUR PROMPT HERE
"""

# ^ If your team decides to write a system prompt do so here, if not leave it empty

system_prompt =  ""

#! Don't change anything below

answer = get_answer(prompt, system_prompt)

output_path = Path(__file__).parent / "ai_output.md"
output_path.write_text(answer, encoding="utf-8")