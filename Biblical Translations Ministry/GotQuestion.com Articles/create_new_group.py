groupNumber = 98

import os
from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir: str = path.dirname(path.abspath(__file__))
targetGroupFolder: str = path.join(currentDir, f"Group {groupNumber}")

originalsFolder: str = path.join(targetGroupFolder, "original")
translatedFolder: str = path.join(targetGroupFolder, "translated")

# create a target group folder in currendir if not already exist, then create two empty folders in it - originals and translated
if not os.path.exists(targetGroupFolder):
    os.makedirs(targetGroupFolder)
    os.makedirs(originalsFolder)
    os.makedirs(translatedFolder)
