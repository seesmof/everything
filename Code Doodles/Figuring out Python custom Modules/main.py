from rich.console import Console
from rich.traceback import install

install()
console = Console()

from misc.main import add, sub, mul, div

console.print(add(1, 2))
