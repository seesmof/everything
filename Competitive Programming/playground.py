memo = {}


def factorial(k):
    if k < 2:
        return 1
    if k not in memo:
        memo[k] = k * factorial(k - 1)
    return memo[k]


import time
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def testFactorial():
    numbers = [5, 3, 4, 5, 3, 2, 4, 2]
    results = {num: 0 for num in numbers}
    for num in numbers:
        startTimer = time.time()
        factorial(num)
        time.sleep(0.1)
        timeTaken = time.time() - startTimer
        results[num] = timeTaken
        console.print(f"Time taken for {num} is {timeTaken:.3f}")


testFactorial()
