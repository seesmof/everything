from os import path
from src.utils.misc import getClothing, readJson
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


currentDir = path.dirname(path.abspath(__file__))
versesPath = path.join(currentDir, "data", "Bible_verses.json")
verses = readJson(versesPath)

console.print(verses, len(verses))
