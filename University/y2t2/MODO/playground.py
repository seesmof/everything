from rich.console import Console
from rich.traceback import install

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

install()
console = Console()


def f(x):
    return -(np.log(x**2 + 1) / np.e**x)


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

    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)")
    plt.title("Golden Search Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.plot([a, b], [f(a), f(b)], "r--", label="Initial Interval")

    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - ratio * (b - a)
        d = a + ratio * (b - a)

        console.print(a, b, c)
        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return (a + b) / 2


def bisectionSearch(f: callable = f, a: float = -1, b: float = 3, tol: float = 1e-5):
    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)")
    plt.title("Bisection Search Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.plot([a, b], [f(a), f(b)], "r--", label="Initial Interval")

    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        console.print(a, b, c)
        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return c


with console.status("Optimizing...", spinner="point"):
    resGolden: float = f"{goldenSearch(a=1):.2f}"
    resBisection: float = f"{bisectionSearch(a=1):.2f}"
    scalarBounded: float = f"{optimize.minimize_scalar(f, bounds=(1, 3)).x:.2f}"

console.print(f"Golden Section Method: {resGolden}")
console.print(f"Bisection Method: {resBisection}")
console.print(f"Bounded Scalar (from scipy): {scalarBounded}")
console.print()
console.print(
    "[green bold]Correct answer found![/green bold]"
    if resGolden == resBisection == scalarBounded
    else "[red bold]Doesn't match![/red bold]"
)

plt.show()
