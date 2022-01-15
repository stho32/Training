#!/usr/bin/python3
import os
import json
import requests
import argparse


def simplify_message(message):
    return message

def get_github_repos(username, page):
    response = requests.get("https://api.github.com/users/" + username + "/repos?page=" + str(page))
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed

def get_stuff_to_look_for() -> list:
    """
    Look in the current directory for any subfolder.
    In this repository those represent the projects that can be implemented.
    """
    result = list()

    for f in os.listdir("."):
        if not os.path.isfile(f):
            if not f.startswith("."):
                result.append(f)

    return result

def get_all_repositories(username: str) -> list:
    page = 1
    result = list()
    repositories = [""]

    while len(repositories) > 0:
        repositories = get_github_repos(username, page)
        for repository in repositories:
            result.append(repository["name"])
        page += 1
    
    result.sort()
    return result

def get_matching_repositories(repositories : list, repositoryPrefix : str) -> list:
    result = list()

    for repository in repositories:
        if (repository.startswith(repositoryPrefix)):
            result.append(repository)
    
    return result

def write_known_implementations_readme(filename : str, repositories : list) -> None:
    with open(filename, 'w') as f:
        f.write('# Known Implementations\n')
        f.write('\n')
        for repository in repositories:
            f.write("- [" + repository + "](https://github.com/stho32/" + repository + ")\n")

def update_known_implementations() -> None:
    print(" - retrieving repositories")
    repositories = get_all_repositories("stho32")
    print(" - retrieving projects")
    projects_to_look_for = get_stuff_to_look_for()

    for project in projects_to_look_for:
        print(" - updating " + project + " ...")
        matching_repositories = get_matching_repositories(repositories, project + "-")
        write_known_implementations_readme(project + "/KnownImplementations.md", matching_repositories)

if __name__ == "__main__":
    update_known_implementations()