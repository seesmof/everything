from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()

number: int = 3000500722
console.print(f"{number:_}")

Amen: str = "Jesus Christ is our Lord"
console.print(f"[bold]{Amen}[/]")

console.print(f"{number = }")
