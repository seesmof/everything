from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def solve(arr: List[int]) -> List[int]:
    prefix = []
    curr = arr[0]
    for num in arr:
        curr *= num
        prefix.append(curr)
    res = []
    console.print(f"{prefix = }")
    prefix = list(reversed(prefix))
    for i, num in enumerate(arr):
        console.print(num)
        curr = num * prefix[i]
        res.append(curr)
    console.print(f"{res = }")


arr = [1, 2, 3, 4]
solve(arr)


def tests() -> None:
    with console.status("[bold]Running tests...[/]"):
        assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]
        assert solve([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    console.print("[bold green]All tests passed![/]")
