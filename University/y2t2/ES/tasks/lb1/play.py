from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

V = (0.00812 * 273 * 756) / ((273 + 25) * 760)
console.print(f"{V:.3f}")

C = (7.584 - 4.583) / (V)
console.print(f"{C:.3f}")
