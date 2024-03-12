from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

arr = [123, 321, 111]
console.print(arr, 3 in arr)
