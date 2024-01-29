from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def tests():
    assert search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
    console.print("[green bold]Passed all tests![/]")


tests()
