"""
Properties: Name, Description, Status, Difficulty

Difficulty: easy, medium, hard (1, 2, 3)
Status: todo, doing, done
"""

from os import path
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from click_shell import shell
import sqlite3

currentDir = path.dirname(path.abspath(__file__))
databasePath = path.join(currentDir, "..", "data", "project_ideas.db")

# help
# add task
# remove task
# list tasks


@shell(
    prompt="> ",
    intro="Welcome to Project Ideas Manager!\nEnter 'help' for list of commands",
)
def pm_shell():
    pass


@pm_shell.command()
def help():
    print(
        """
Here is a list of all commands:

help: See this list
add: Add a new project idea
remove: Remove a project idea
show: Show all project ideas
"""
    )


def getNewIdeaData():
    name = input("Project Name *: ")
    description = input("Project Description: ")
    status = input("Project Status: ")
    difficulty = input("Project Difficulty: ")

    description = description if description else None
    status = status if status else "todo"
    difficulty = difficulty if difficulty else 1


@pm_shell.command()
def add():
    name, description, status, difficulty = getNewIdeaData()


if __name__ == "__main__":
    pm_shell()
