from os import path
import sqlite3
from rich.console import Console
from rich.traceback import install

install()
console = Console()


currentDir = path.dirname(path.abspath(__file__))
dbPath = path.join(currentDir, "data", "people.db")

connection = sqlite3.connect(dbPath)

connection.execute(
    "create table if not exists people (firstName text, lastName text, age integer)"
)

peopleNames = [
    ("Patrick", "Meyer", "21"),
    ("Tillie", "Martin", "25"),
    ("Norman", "Massey", "21"),
    ("Joshua", "Richards", "25"),
    ("Adeline", "Watkins", "30"),
]

connection.executemany(
    "insert into people (firstName, lastName, age) values (?, ?, ?)", peopleNames
)
connection.commit()

console.print("All done!")

console.print(connection.execute("select * from people").fetchall())

connection.close()
