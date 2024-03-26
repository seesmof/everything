groupNumber = 98

import os
from os import path
import shutil
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir: str = path.dirname(path.abspath(__file__))
targetGroupFolder: str = path.join(currentDir, f"Group {groupNumber}")

originalsFolder: str = path.join(targetGroupFolder, "original")
translatedFolder: str = path.join(targetGroupFolder, "translated")


def copyOriginalDocs() -> None:
    # check if originals folder is not empty
    if len(os.listdir(originalsFolder)) > 0:
        for file in os.listdir(originalsFolder):
            originalPath = path.join(originalsFolder, file)
            if path.isfile(originalPath):
                base, extension = path.splitext(file)
                targetFile = f"{base}_Ukrainian{extension}"
                targetPath = path.join(translatedFolder, targetFile)
                console.print(
                    f"[yellow]Copying[/yellow] {file} [yellow]to[/yellow] {targetFile}"
                )
                shutil.copy2(originalPath, targetPath)
    else:
        console.print("[red]No original files to copy[/]")
