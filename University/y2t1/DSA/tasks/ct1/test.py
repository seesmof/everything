from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md

install()
consoleTheme = Theme(
    {
        "warning": "bold yellow",
        "error": "bold red",
        "success": "bold green",
        "info": "bold blue",
    }
)
console = Console(theme=consoleTheme)

console.print("[pink1]Hey Barbie[/]")
console.print("[thistle1]Hey Ken[/]")
console.print("[red1]Hey Marcus[/]")
