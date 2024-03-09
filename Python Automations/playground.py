from math import prod
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def decarteus_multiplieous(one: list[int], two: list[int]):
    return [a * b for a in one for b in two]


arr = [1, 2, 3]
two = [3, 5, 6]
res = decarteus_multiplieous(arr, two)
console.print(res)

console.print(md("# Thank you Agnus Dei 🙏💗✝️"))
