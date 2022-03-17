#!/usr/bin/python3
"""
    It has become quite cumbersome to get the names for repositories right.
    This tool will help you.
"""

def give_me_that_name():
    project = input("Which project do you want to implement? : ")
    projecttype = input("What kind of project shall it be (Console, WebApp, WebApi, GUI, Library)? : ")
    operating_system = input("Win32, Win64, Linux, MacOS, X? : ")    
    programming_language = input("C, CSharp, JavaScript, Python... : ")
    iteration = input("three digit number as iteration xxx : ")
    variant = input("variant (Vxxx) if needed : ")

    complete_name = f"{project}-{projecttype}-{operating_system}-{programming_language}-{iteration}"
    if variant != "":
        complete_name += variant

    return complete_name

if __name__ == "__main__":
    complete_name = give_me_that_name()
    print(f"complete name : {complete_name}")
