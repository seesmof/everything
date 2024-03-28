def f(x):
    return (x - 2) ** 2


from rich.console import Console
from rich.traceback import install
from scipy import optimize

install()
console = Console()

res = optimize.minimize_scalar(f, bounds=(-1, 3), method="golden")
console.print(f"Відповідь: {res.x}")
