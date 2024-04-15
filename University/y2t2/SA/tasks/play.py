from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

per = 20.5 / 100
bef = 7052.31
res = bef * per
console.print(f"Sum after tax: {res}")
