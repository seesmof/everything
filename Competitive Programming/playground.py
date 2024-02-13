from typing import List
from functools import cache
import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()

l, k, d, x = map(int, input().split())
print(l + k + d + x)
