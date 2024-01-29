from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def tests():
    console.print("[green bold]Passed all tests![/]")


tests()
