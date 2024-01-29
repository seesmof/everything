from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def closeDuplicatesBruteForce(nums: List[int], k: int) -> bool:
    for L in range(len(nums)):
        for R in range(L + 1, min(L + k, len(nums))):
            if nums[L] == nums[R]:
                return True
    return False


def closeDuplicates(nums: List[int], k: int) -> bool:
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False


arr = [1, 2, 3, 2, 3, 3]
k = 3
res = closeDuplicatesBruteForce(arr, k)
console.print(
    f"[bold]Brute Force[/]: For {arr} and a window of size {k} the result is {res}"
)
res = closeDuplicates(arr, k)
console.print(
    f"[bold]Hash Set[/]: For {arr} and a window of size {k} the result is {res}"
)
