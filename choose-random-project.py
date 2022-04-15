"""
    Choose a random project
    
    Uses the data contained in this repository to 
    create a challenge for you, giving you an individual
    name for the project to use in github.

    A random project will be described using: 
    - the project ID
    - the language you shall use
    - the type of application
    - random mutators, if they are selected
"""
import json
import random
import os

def read_json(filename) -> dict:
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

project_categories = read_json("data/projects.json")
project_types = read_json("data/project_types.json")
operating_systems = read_json("data/operating_systems.json")
mutators = read_json("data/mutators.json")
programming_languages = read_json("data/programming_languages.json")

random_category = random.choice(project_categories)
random_project = random.choice(random_category["projects"])
random_project_type = random.choice(project_types)
random_operating_system = random.choice(operating_systems)
random_programming_language = random.choice(programming_languages)

random_mutators = []

for mutator in mutators:
    random_number = random.randint(1, 100)
    if random_number <= mutator["probabilityInPercent"]:
        random_mutators.append(mutator)

mutator_description = ""
for mutator in random_mutators:
    mutator_description += mutator["id"]

#os.system("clear")
print("")
print("Your Challenge: ")
print("")
print("    from the category    : " + random_category["name"])
print("    implement the project: " + random_project["id"] + " " + random_project["title"])
print("    as                   : " + random_project_type)
print("    using                : " + random_programming_language)
print("    supporting at least  : " + random_operating_system)
print("")

if len(random_mutators) > 0:
    print("    To make it even more fun, we have coosen the following mutators:")
    print("")
    for mutator in random_mutators:
        print("    - " + mutator["id"] + " : " + mutator["text"])
    
print("")
print("")

if mutator_description != "":
    print("  project name for github: " + random_project["id"] + "-" + random_project_type + "-" + random_operating_system + "-" + random_programming_language + "_" + mutator_description)
else:
    print("  project name for github: " + random_project["id"] + "-" + random_project_type + "-" + random_operating_system + "-" + random_programming_language)

print("")
print("See https://github.com/stho32/Training for the needed details like the project description.")
print("")
