from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def maxProfit(prices: List[int]) -> int:
    if prices == sorted(prices, reverse=True):
        return 0

    top = 0
    for buy in range(len(prices)):
        pricesAfterBuy = prices[buy:]
        sell = max(pricesAfterBuy)
        top = max(top, sell - prices[buy])
    return top


def tests():
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    console.print("[green bold]All tests passed![/]")


tests()
