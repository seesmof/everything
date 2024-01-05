from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

colorsToTest = [
    "grey0",
    "bright_black",
    "grey37",
    "grey53",
    "light_slate_grey",
]
for color in colorsToTest:
    console.print(md(f"## {color}"), style=color)
