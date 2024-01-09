from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
membersDbPath = path.join(currentDir, "..", "data", "members.db")
alternativePath = f"{currentDir}\..\data\members.db"

console.print(membersDbPath == alternativePath)
