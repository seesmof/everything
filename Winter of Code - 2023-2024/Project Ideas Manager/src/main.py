"""
Properties: Name, Description, Status, Difficulty

Difficulty: easy, medium, hard (1, 2, 3)
Status: todo, doing, done
"""

from os import path
from rich.table import Table
from rich.console import Console
from rich.traceback import install
from click_shell import shell
import sqlite3

from utills import (
    Difficulty,
    Status,
    addTask,
    createTable,
    getNewIdeaData,
    getTableRows,
)

install()
console = Console()


currentDir = path.dirname(path.abspath(__file__))
databasePath = path.join(currentDir, "..", "data", "project_ideas.db")
conn = sqlite3.connect(databasePath)
c = conn.cursor()

# help
# add task
# remove task
# edit task
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


@pm_shell.command()
def add():
    name, description, status, difficulty = getNewIdeaData(console=console)
    if not name:
        console.print("Name cannot be empty")
        return

    createTable(connection=conn, cursor=c)
    addTask(
        name=name,
        description=description,
        status=status,
        difficulty=difficulty,
        connection=conn,
        cursor=c,
    )
    console.print("Task added successfully")


@pm_shell.command()
def show():
    rows = getTableRows(cursor=c, console=console)
    t = Table("ID", "Name", "Description", "Status", "Difficulty")

    for row in rows:
        id, name, description, status, difficulty = row
        t.add_row(
            f"[bold]{id}[/]",
            f"{name}",
            f"{description[0].upper() + description[1:]}" if description else "",
            f"[blue]{status.title()}[/]"
            if status == "todo"
            else f"[yellow]{status.title()}[/]"
            if status == "doing"
            else f"[green]{status.title()}[/]",
            f"[green]{difficulty}[/]"
            if difficulty == "easy"
            else f"[yellow]{difficulty}[/]"
            if difficulty == "medium"
            else f"[red]{difficulty}[/]",
        )

    console.print(t)


if __name__ == "__main__":
    pm_shell()
