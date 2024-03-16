import json
from os import path
import os
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir: str = path.dirname(path.abspath(__file__))
mainFilePath: str = path.join(currentDir, "AMP to UKR", "main.json")
main = {}
with open(mainFilePath, "r", encoding="utf-8") as jsonFile:
    main = json.load(jsonFile)
for Testament in main:
    for Book in main[Testament]:
        ChaptersCount = Book["Chapters_Count"]
        Chapters = {f"{i+1}": {"1": ""} for i in range(ChaptersCount)}
        Book["Chapters"] = Chapters
with open(mainFilePath, "w", encoding="utf-8") as jsonFile:
    json.dump(main, jsonFile, indent=2)
