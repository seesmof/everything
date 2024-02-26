from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from functools import wraps
from time import perf_counter


def memoize(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


startTimer = perf_counter()
with console.status("[bold green]Calculating..."):
    res = fib(100)
timeTaken = perf_counter() - startTimer
console.print(f"Calculated {res = } in {timeTaken:.1f} seconds")
