from os import path
import sqlite3
from rich.console import Console
from rich.traceback import install

from utilities import *

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
dbPath = path.join(currentDir, "data", "members.db")
scriptPath = path.join(currentDir, "members_creation.sql")

connect = sqlite3.connect(dbPath)
cursor = connect.cursor()

createMembersDb(cursor=cursor, path=scriptPath) if not path.exists(
    dbPath
) else readMembersDb(cursor=cursor, consoleObject=console)

connect.commit()
cursor.close()
connect.close()
