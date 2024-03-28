from rich.console import Console
from rich.traceback import install

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

install()
console = Console()


def f(x):
    return (x - 2) ** 2


x = np.linspace(-1, 3, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="(x-2)^2")
plt.title("Plot of (x-2)^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)


def goldenSearch(f: callable = f, a: float = -1, b: float = 3, tol: float = 1e-5):
    ratio = (5**0.5 - 1) / 2
    c = b - ratio * (b - a)
    d = a + ratio * (b - a)
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - ratio * (b - a)
        d = a + ratio * (b - a)
    return (a + b) / 2


def bisectionSearch(f: callable = f, a: float = -1, b: float = 3, tol: float = 1e-5):
    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


with console.status("Оптимізуємо...", spinner="point"):
    # limiting floating point precision to 2 digits after comma
    resGolden: float = f"{goldenSearch():.2f}"
    testGolden: float = f"{optimize.golden(f):.2f}"
    resBisection: float = f"{bisectionSearch():.2f}"
    testBisection: float = f"{optimize.bisect(f, -1, 2):.2f}"
    # scipy bisect не працює для [-1, 3], але чомусь працює для [-1, 2]. результат правильний видає

console.print(f"Golden Section Method: {resGolden}")
console.print(f"Golden Section Method (from scipy): {testGolden}")
console.print(f"Bisection Method: {resBisection}")
console.print(f"Bisection Method (from scipy): {testBisection}")
console.print()
console.print(
    "[green bold]Correct answer found![/green bold]"
    if resGolden == testGolden
    and resBisection == testBisection
    and resGolden == testGolden == resBisection == testBisection
    else "[red bold]Doesn't match![/red bold]"
)

plt.show()
