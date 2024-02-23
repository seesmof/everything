from time import sleep
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

make = [6, 9, 8, 7, 5, 4, 9, 1, 0]
with console.status("Working on it..."):
    for i in make:
        sleep(0.5)
