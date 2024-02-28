import random
import pyperclip
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


arr = [[random.choice([0, 1]) for _ in range(10)] for _ in range(5)]
console.print(arr)
pyperclip.copy(str(arr))
