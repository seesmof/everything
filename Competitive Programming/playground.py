from os import path
import re
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
dataFolder = path.join(currentDir, "data")
lineyFile = path.join(dataFolder, "195-lotta-lines.txt")

lines = []

with open(lineyFile, "r") as file:
    for line in file:
        lines.append(line.strip())

tenthLine = lines[9] if len(lines) > 9 else "No more lines"
console.print(tenthLine)
