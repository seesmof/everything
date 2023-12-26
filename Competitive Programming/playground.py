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
    numbers = [500, 300, 400, 500, 300, 200, 400, 200]
    results = {num: 0 for num in numbers}
    for num in numbers:
        startTimer = time.time()
        factorial(num)
        time.sleep(0.1)
        timeTaken = time.time() - startTimer
        results[num] = timeTaken
        console.log(f"Time taken for {num} is {timeTaken}")


testFactorial()
