import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def reverse(n: int) -> int:
    string = str(n)
    neg = False
    if "-" in string:
        string = string[1:]
        neg = True
    reverse = string[::-1]
    res = int(reverse)
    return res if not neg else -res


def findSqrt(n: int) -> int:
    if n < 2:
        return n
    low, high = 1, n
    while low <= high:
        guess = (low + high) / 2
        if guess * guess == n:
            return guess
        elif guess * guess < n:
            low = guess + 1
        else:
            high = guess - 1
    return high


n = "-123"
res = reverse(n)
console.print(f"Reverse of {n} is {res}")
