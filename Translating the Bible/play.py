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
targetFolderPath: str = path.join(currentDir, "Сучасний Американо-Український - САУ")
mainFilePath: str = path.join(targetFolderPath, "main.json")
target = path.join(currentDir, "Коментарі до Біблії від Метью Генрі")

with open(mainFilePath, "r", encoding="utf-8") as jsonFile:
    main = json.load(jsonFile)

for Testament in main:
    # create folder in targetFolder for each Testament
    targetTestamentFolder: str = path.join(target, Testament)
    if not os.path.exists(targetTestamentFolder):
        os.makedirs(targetTestamentFolder)

    for Book in main[Testament]:
        Book_Name = Book["Name"]
        # create folder in targetFolder for each Book
        targetTestamentBookFolder: str = path.join(targetTestamentFolder, Book_Name)
        if not os.path.exists(targetTestamentBookFolder):
            os.makedirs(targetTestamentBookFolder)

        for Chapter in Book["Chapters"]:
            Chapter_File = f"{Chapter}.md"
            # create file in targetFolder for each Chapter
            targetTestamentBookChapterFile: str = path.join(
                targetTestamentBookFolder, Chapter_File
            )
            if not os.path.exists(targetTestamentBookChapterFile):
                with open(
                    targetTestamentBookChapterFile, "w", encoding="utf-8"
                ) as mdFile:
                    # just create an empty file
                    mdFile.write("")
