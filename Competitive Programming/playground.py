from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    res = 0

    for sell in prices:
        if sell < buy:
            buy = sell
        else:
            res = max(res, sell - buy)
    return res


def tests():
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    console.print("[green bold]All tests passed![/]")


tests()
