from week3.Part_3_Prompt.prompt_test import get_answer
from pathlib import Path

user_question = "Where can I go in Ottawa to see a doctor who speaks Arabic?"
health_resources = [
    {
        "name": "Ottawa Community Health Centre",
        "service": "Primary healthcare and community health services",
        "address": "123 Main Street, Ottawa, ON",
        "phone": "613-555-0142",
        "hours": "Monday–Friday, 8:30 AM–4:30 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Open to Ottawa residents. Some services may have additional requirements.",
        "cost": "Many services are free or covered by provincial health insurance."
    },
    {
        "name": "Riverside Walk-In Clinic",
        "service": "Walk-in medical appointments",
        "address": "456 Riverside Drive, Ottawa, ON",
        "phone": "613-555-0187",
        "hours": "Monday–Saturday, 9:00 AM–6:00 PM",
        "languages": ["English", "French"],
        "eligibility": "Appointments depend on availability.",
        "cost": "OHIP-covered services are generally free."
    },
    {
        "name": "Newcomer Dental Support Program",
        "service": "Dental care assistance for eligible newcomers",
        "address": "789 Bank Street, Ottawa, ON",
        "phone": "613-555-0199",
        "hours": "Tuesday–Friday, 10:00 AM–4:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Eligibility depends on immigration status and household income.",
        "cost": "Free for eligible participants."
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