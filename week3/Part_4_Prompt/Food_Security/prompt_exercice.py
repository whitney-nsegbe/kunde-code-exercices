from week3.Part_4_Prompt.prompt_test import get_answer
from pathlib import Path

user_question = "Where can I get free food or groceries in Ottawa?"
food_resources = [
    {
        "name": "Ottawa Community Food Bank",
        "service": "Food hampers and emergency food assistance",
        "address": "200 Industrial Avenue, Ottawa, ON",
        "phone": "613-555-0133",
        "hours": "Monday–Friday, 9:00 AM–4:00 PM",
        "languages": ["English", "French"],
        "eligibility": "Available to people experiencing food insecurity.",
        "cost": "Free."
    },
    {
        "name": "Neighbourhood Community Pantry",
        "service": "Free groceries and pantry items",
        "address": "50 Elm Street, Ottawa, ON",
        "phone": "613-555-0172",
        "hours": "Wednesday and Saturday, 10:00 AM–2:00 PM",
        "languages": ["English", "French"],
        "eligibility": "Open to community members. No appointment required.",
        "cost": "Free."
    },
    {
        "name": "Newcomer Grocery Support Program",
        "service": "Food assistance and grocery gift cards",
        "address": "300 Rideau Street, Ottawa, ON",
        "phone": "613-555-0155",
        "hours": "Monday–Thursday, 10:00 AM–3:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "For eligible newcomer families experiencing financial difficulty.",
        "cost": "Free for eligible participants."
    }
]
prompt = f"""
Answer the user's question using ONLY the food resource information provided below.

Identify the resources that are relevant to the user's request. For each relevant resource, explain:
- the organization's name
- what food assistance it provides
- where it is located
- its phone number
- its hours
- available languages
- eligibility requirements
- cost

Make the answer clear and easy to scan. Prioritize information that would help someone decide which resource they can actually use.

Do not invent, assume, or add information that is not provided in the resources. If an important piece of information is missing, say that it was not provided.

If none of the resources are relevant to the user's question, clearly say that the provided resources do not contain a suitable option.

User question:
{user_question}

Food resources:
{food_resources}
"""

# ^ If your team decides to write a system prompt do so here, if not leave it empty

system_prompt =  ""

#! Don't change anything below

answer = get_answer(prompt, system_prompt)

output_path = Path(__file__).parent / "ai_output.md"
output_path.write_text(answer, encoding="utf-8")