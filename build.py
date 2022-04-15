"""
    Creates documentation files in a common format
    
    This repository has grown and now contains a big collection
    of project descriptions. That makes ensuring a common
    quality a problem.
    So I now try out if having data files works, combined
    with the automated creation of md files.
"""
import json
import io

def read_project_categories() -> dict:
    with open('data/projects.json') as json_file:
        data = json.load(json_file)
        return data

def create_project_markdown(project, category) -> str:
    result = []

    index_filename = get_project_index_filename(project, category)
    list_item = "- [" + project["id"] + "]"
    list_item += "(" + index_filename + ") "
    list_item += "\"" + project["nickname"] + "\", "
    list_item += project["title"]

    result.append(list_item)

    return '\n'.join(result)

def create_category_markdown(category) -> str:
    result = []

    result.append("# " + category["name"])
    result.append("")
    result.append(category["description"])
    result.append("")
    result.append("")

    for project in category["projects"]:
        result.append(create_project_markdown(project, category))

    return '\n'.join(result)

def get_project_index_filename(project, category) -> str:
    return project["id"] + "/README.md"

def get_category_index_filename(category) -> str:
    return category["folder"] + "/README.md"

def log(text):
    print("  - " + text)

def write_file(filename, text):
    with io.open(filename, 'w', encoding='utf8') as f:
        f.write(text)

if __name__ == "__main__":
    project_categories = read_project_categories()

    for category in project_categories:
        log("processing " + category["name"])
        content = create_category_markdown(category)
        filename = get_category_index_filename(category)
        write_file(filename, content)