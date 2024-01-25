import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


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


question = [
    inquirer.Text(
        "number",
        message="Enter number",
        validate=lambda _, x: x.isnumeric() and int(x) > 0,
    )
]
answer = inquirer.prompt(question)
n = int(answer["number"])
res = findSqrt(n)
console.print(f"Square root of {n} is {res}")
