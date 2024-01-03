from time import sleep
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

with console.status("Processing all the tracks..."):
    for i in range(12):
        sleep(0.1)
