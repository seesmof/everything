from enum import Enum
import sqlite3
from rich.markdown import Markdown as md


class Status(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


def getTableRows(cursor: sqlite3.Cursor, console) -> list:
    try:
        cursor.execute("SELECT * FROM project_ideas")
    except sqlite3.OperationalError:
        createTable(connection=cursor.connection, cursor=cursor)
    rows = cursor.fetchall()
    if not rows:
        console.print("No project ideas found. Create one with 'add'")
        return []
    return rows


def createTable(cursor: sqlite3.Cursor, connection: sqlite3.Connection) -> None:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS project_ideas (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, status TEXT, difficulty TEXT)"
    )
    connection.commit()


def addTask(
    name: str,
    description: str,
    status: Status,
    difficulty: Difficulty,
    connection: sqlite3.Connection,
    cursor: sqlite3.Cursor,
):
    cursor.execute(
        "INSERT INTO project_ideas (name, description, status, difficulty) VALUES (?, ?, ?, ?)",
        (name, description, status.value, difficulty.value),
    )
    connection.commit()


def getNewIdeaData(console) -> tuple:
    console.print()
    name = input("Project Name - Required\n: ")
    description = input("Project Description - Can be empty\n: ")
    status = input("Project Status - todo | doing | done. Default is todo\n: ")
    difficulty = input("Project Difficulty - easy | medium | hard. Default is easy\n: ")
    console.print()

    name = name.title() if name else None
    description = description if description else None
    status = Status(status) if status in [s.value for s in Status] else Status.TODO
    difficulty = (
        Difficulty(difficulty)
        if difficulty in [d.value for d in Difficulty]
        else Difficulty.EASY
    )

    return name, description, status, difficulty
