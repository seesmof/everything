from rich.console import Console
from rich.traceback import install

install()
console = Console()


def quickSort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [el for el in arr if el < pivot]
    eq = [el for el in arr if el == pivot]
    more = [el for el in arr if el > pivot]

    return quickSort(less) + eq + quickSort(more)


arr = [19, 3, 16, 5, 7, 6, 9, 11, 21, 45]
res = quickSort(arr)
console.print(f"Before sorting: {arr}\nAfter sorting: {res}")
arr = res


def binarySearch(arr: list[int], n: int) -> int:
    console.print(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == n:
            return mid
        if guess > n:
            right = mid - 1
        else:
            left = mid + 1

    return -1


n = 16
res = binarySearch(arr, n)
console.print(f"Element {n} is at index: {res}")
