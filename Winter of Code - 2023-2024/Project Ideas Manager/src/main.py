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
from enum import Enum


class Status(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


currentDir = path.dirname(path.abspath(__file__))
databasePath = path.join(currentDir, "..", "data", "project_ideas.db")
conn = sqlite3.connect(databasePath)
c = conn.cursor()

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
    console.print()
    name = input("Project Name - Required\n: ")
    description = input("Project Description - Can be empty\n: ")
    status = input("Project Status - todo | doing | done. Default is todo\n: ")
    difficulty = input("Project Difficulty - easy | medium | hard. Default is easy\n: ")
    console.print()

    name = name if name else None
    description = description if description else None
    status = Status(status) if status in [s.value for s in Status] else Status.TODO
    difficulty = (
        Difficulty(difficulty)
        if difficulty in [d.value for d in Difficulty]
        else Difficulty.EASY
    )

    return name, description, status, difficulty


def createTable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS project_ideas (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, status TEXT, difficulty TEXT)"
    )
    conn.commit()


def addTask(name, description, status, difficulty):
    c.execute(
        "INSERT INTO project_ideas (name, description, status, difficulty) VALUES (?, ?, ?, ?)",
        (name, description, status.value, difficulty.value),
    )
    conn.commit()


@pm_shell.command()
def add():
    name, description, status, difficulty = getNewIdeaData()
    if not name:
        console.print("Name cannot be empty")
        return

    createTable()
    addTask(name, description, status, difficulty)
    console.print("Task added successfully")


def showTasks():
    try:
        c.execute("SELECT * FROM project_ideas")
    except sqlite3.OperationalError:
        createTable()
    rows = c.fetchall()
    if not rows:
        console.print("No project ideas found. Create one with 'add'")
        return

    t = Table("ID", "Name", "Description", "Status", "Difficulty")

    for row in rows:
        t.add_row(
            str(row[0]),
            str(row[1]),
            str(row[2]),
            str(row[3]),
            str(row[4]),
        )

    console.print(t)


@pm_shell.command()
def show():
    showTasks()


if __name__ == "__main__":
    pm_shell()
