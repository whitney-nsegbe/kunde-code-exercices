from week3.Part_3_Prompt.prompt_test import get_answer
from pathlib import Path

user_question = "Where can I go in Ottawa if I need help finding affordable housing?"

housing_resources = [
    {
        "name": "Ottawa Affordable Housing Network",
        "service": "Affordable housing information and housing applications",
        "address": "100 Laurier Avenue, Ottawa, ON",
        "phone": "613-555-0123",
        "hours": "Monday–Friday, 9:00 AM–5:00 PM",
        "languages": ["English", "French"],
        "eligibility": "Eligibility varies by housing program.",
        "cost": "Housing costs vary depending on the program."
    },
    {
        "name": "Newcomer Housing Support Centre",
        "service": "Housing navigation and support finding temporary accommodation",
        "address": "250 Somerset Street, Ottawa, ON",
        "phone": "613-555-0166",
        "hours": "Monday–Friday, 8:00 AM–4:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Services are available to newcomers to Ottawa.",
        "cost": "Support services are free."
    },
    {
        "name": "Emergency Shelter Information Line",
        "service": "Information about emergency shelters and available beds",
        "address": "Phone service only",
        "phone": "613-555-0111",
        "hours": "24 hours a day, 7 days a week",
        "languages": ["English", "French"],
        "eligibility": "For people experiencing homelessness or needing emergency shelter.",
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