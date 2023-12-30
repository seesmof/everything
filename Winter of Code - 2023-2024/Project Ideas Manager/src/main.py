from os import path
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install
from click_shell import shell
import sqlite3

from utills import (
    addTask,
    createTable,
    getNewIdeaData,
    getTableRows,
)

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
databasePath = path.join(currentDir, "..", "data", "project_ideas.db")
connection = sqlite3.connect(databasePath)
cursor = connection.cursor()


@shell(
    prompt="> ",
    intro="Welcome to Project Ideas Manager!\nEnter 'help' for list of commands",
)
def pm_shell():
    pass


@pm_shell.command()
def help():
    console.print(
        md(
            """
This CLI tool helps you manage your project ideas. You can use it to add, remove and edit your project ideas as well as assign them different properties like `status` and `difficulty`.

Here is a list of all commands:

- help: See this list
- add: Add a new project idea
- remove: Remove a project idea
- edit: Edit a project idea
- show: Show all project ideas
- exit: Exit the shell
"""
        )
    )


@pm_shell.command()
def add():
    name, description, status, difficulty = getNewIdeaData(console=console)
    if not name:
        console.print("[red]Name cannot be empty[/]")
        return

    createTable(connection=connection, cursor=cursor)
    addTask(
        name=name,
        description=description,
        status=status,
        difficulty=difficulty,
        connection=connection,
        cursor=cursor,
    )
    console.print("[green]Task added successfully[/]")


@pm_shell.command()
def remove():
    rows = getTableRows(cursor=cursor, console=console)
    if not rows:
        console.print("[red]No project ideas found[/]. Create one with 'add'")
        return
    id = input("Enter the ID of the project idea you want to remove: ")
    cursor.execute("DELETE FROM project_ideas WHERE id = ?", (id,))
    connection.commit()
    console.print("[green]Task removed successfully[/]")


@pm_shell.command()
def edit():
    rows = getTableRows(cursor=cursor, console=console)
    if not rows:
        console.print("[red]No project ideas found[/]. Create one with 'add'")
        return
    id = input("Enter the ID of the project idea you want to edit: ")
    name, description, status, difficulty = getNewIdeaData(console=console)
    if not name:
        console.print("[red]Name cannot be empty[/]")
        return
    cursor.execute(
        "UPDATE project_ideas SET name = ?, description = ?, status = ?, difficulty = ? WHERE id = ?",
        (name, description, status.value, difficulty.value, id),
    )
    connection.commit()
    console.print("[green]Task edited successfully[/]")


@pm_shell.command()
def show():
    rows = getTableRows(cursor=cursor, console=console)
    if not rows:
        return
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
            f"[green]{difficulty.title()}[/]"
            if difficulty == "easy"
            else f"[yellow]{difficulty.title()}[/]"
            if difficulty == "medium"
            else f"[red]{difficulty.title()}[/]",
        )

    console.print(t)


if __name__ == "__main__":
    pm_shell()
