from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md

install()
console = Console()

console.print(f"{'nine' in 'ninefourthreefivefouronetwosixniner'}")
