from typing import List
from functools import cache
import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def getN() -> int:
    askForN = [
        inquirer.Text("n", message="Enter n", validate=lambda _, x: x.isnumeric())
    ]
    lookForN = inquirer.prompt(askForN)
    return int(lookForN["n"])


allOptions = [1, 2, 5, 10, 20, 50, 100, 200, 500]
allOptions = sorted(allOptions, reverse=True)
n = int(input())
takes = 0
for meow in allOptions:
    fit = n // meow
    takes += fit
    n -= fit * meow
    if n == 0:
        break
print(takes)
