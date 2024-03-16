from os import path
import os
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

patternsToRemove: list[str] = ["🎤 ", "yt1s.com -  "]
targetDir: str = "C:\\Users\\seesm\\Downloads\\"
replacePattern: dict = {"  ": " - "}


def removePatterns(dir: str, patterns: list[str]) -> None:
    files = [f for f in os.listdir(dir)]

    for file in files:
        newName = file
        for pattern in patterns:
            if newName.startswith(pattern):
                newName = newName[len(pattern) :]
        targetFile = path.join(dir, newName)
        if newName != file:
            try:
                os.rename(path.join(dir, file), targetFile)
                console.print(f"Renamed {file} to {newName}")
            except FileExistsError:
                console.print(f"Error: {newName} already exists.")
            except Exception as e:
                console.print(f"Error renaming {file}: {e}")
        else:
            console.print(f"No change for {file}")


def replaceSpaces(dir: str, replace: dict) -> None:
    files = [f for f in os.listdir(dir)]

    for file in files:
        newName = file
        for pattern, replacement in replace.items():
            newName = newName.replace(pattern, replacement)
        targetFile = path.join(dir, newName)
        if newName != file:
            try:
                os.rename(path.join(dir, file), targetFile)
                console.print(f"Renamed {file} to {newName}")
            except FileExistsError:
                console.print(f"Error: {newName} already exists.")
            except Exception as e:
                console.print(f"Error renaming {file}: {e}")
        else:
            console.print(f"No change for {file}")
