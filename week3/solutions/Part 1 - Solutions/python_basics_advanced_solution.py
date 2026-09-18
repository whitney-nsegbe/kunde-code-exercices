# Week 3  "Build a Resource" ADVANCED EXTENSIONS (STARTER)
# The basic data structure is provided below so you can jump straight
# into the harder part of each extension.

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


# EXTENSION A -- Nested data
# Add "hours" and "languages" to each dictionary above.
# Make "languages" a list INSIDE the dictionary (a resource can support
# more than one language).


# Answer these:
# 1. How would you access just the languages for one resource?
print(list_of_resource[0]["languages"])
# 2. How would you access just the first language in that list?
print(list_of_resource[0]["languages"][0])


# EXTENSION B -- Loop through the whole list
# Write a function that prints the name of EVERY resource in the list
# (not just the first one).
def resource_loop(resource):
    for i in resource:
        print( i["name"])

# Answer this:
# 3. What would you need to change if list_of_resource had 50 items
#    instead of 2? Would your function still work?
#


# EXTENSION C -- A tiny search function
# Write a function called "find_resource_by_name" that takes a name and
# searches list_of_resource for a matching resource, then returns it.
#
# This is a small preview of something called "retrieval" -- you'll see
# this idea again in a few weeks.

def find_resource_by_name(name):
    for i in list_of_resource:
        if i["name"] == name:
            return i
    
    return None

print(find_resource_by_name("Ottawa Food "))
# Answer this:
# 4. What does your function return if no resource matches the name given?
#    Is that the behavior you want? Why or why not?
#