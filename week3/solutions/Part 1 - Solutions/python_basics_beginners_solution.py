# Week 3 — "Build a Resource" — CORE EXERCISE

# TASK 1 — Variable
question = "where can I find a hospital"

# TASK 2 — List
needs = ["health card", "SIN"]

# TASK 3 — Dictionary
resource = {
    "name": "Ottawa Central Hospital",
    "phone_number": "613-899-2820",
    "address": "222 Main Road"
}

# TASK 4 — List of dictionaries
list_of_resource = [
    {
        "name": "Ottawa Central Hospital",
        "phone_number": "613-899-2820",
        "address": "222 Main Road"
    },
    {
        "name": "Ottawa Food Bank",
        "phone_number": "613-555-4321",
        "address": "88 Bank Street"
    }
]

# TASK 5 — Function
def final_output(user_name):
    return (
        "Hi " + user_name +
        ", you will need: " + ", ".join(needs) +
        ". Here is one resource: " + list_of_resource[0]["name"]
    )

print(final_output("Whitney"))


# BONUS — same thing, using a loop instead of .join()
def final_output_loop(user_name):
    needs_string = ""
    for i, item in enumerate(needs):
        needs_string += item
        if i < len(needs) - 1:
            needs_string += ", "

    return (
        "Hi " + user_name +
        ", you will need: " + needs_string +
        ". Here is one resource: " + list_of_resource[0]["name"]
    )

print(final_output_loop("Whitney"))