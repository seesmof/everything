from time import sleep
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

with console.status("Monkey jumping...", spinner="point"):
    sleep(6)
