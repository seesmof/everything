from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()

"""
"""


def solve(s: str) -> int:
    # form a list of all substrings
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            res.append(s[i:j])
    console.print(res)


def tests() -> None:
    with console.status("[bold]Running tests...[/]"):
        assert solve("abcabcbb") == 3, "Should be 3"
        assert solve("bbbbb") == 1, "Should be 1"
        assert solve("pwwkew") == 3, "Should be 3"
        assert solve("") == 0, "Should be 0"
        assert solve("a") == 1, "Should be 1"
        assert solve("dvdf") == 3, "Should be 3"
        assert solve("babad") == 3, "Should be 3"
        assert solve("cbbd") == 2, "Should be 2"
    console.print("[bold green]All tests passed![/]")


solve("babad")
