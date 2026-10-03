resources = [
    {"name": "Sandy Hill Community Health Centre", "category": "healthcare", "source": "KundeCodeResource"},
    {"name": "Ottawa Food Bank", "category": "food", "source": "KundeCodeResource"},
    {"name": "Legal Aid Ottawa", "category": "legal", "source": "Google"},
    {"name": "Random Food Blog", "category": "food", "source": "Google"},
    {"name": "Community Legal Clinic", "category": "legal", "source": "KundeCodeResource"},
]

# let's simulate a RAG implementation, return all the results that come from our internal documents and match the category the user is asking for choose between : legal, food, healthcare

#retrieve
def find_resources(category):
    results = []

    for resource in resources:
        if resource["category"] == category and resource["source"] == "KundeCodeResource":
            results.append(resource)

    return results

# start with print(find_resources("food"))
# show them how it returns nothing if we put an invalid ressource
result = find_resources("food")

print(find_resources("food"))
print(find_resources("school"))

# Augment
result_list = []
for r in result:
    result_list.append(r["name"])

# This is an exemple of the "generation part", f string stands for the llm
print(f"""
Here are the trusted ressources: {", ".join(result_list)}
""")
