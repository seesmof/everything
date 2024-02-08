from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def replace(nums: [int]) -> [int]:
    for i, num in enumerate(nums[:-1]):
        nums[i] = max(nums[i + 1 :])
    nums[-1] = -1
    return nums


arr = [17, 18, 5, 4, 6, 1]
res = replace(arr)
console.print(f"{arr} -> {res}")
