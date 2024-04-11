from rich.console import Console
from rich.traceback import install

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

install()
console = Console()


def twenty(x):
    return (x - 2) ** 2


def nineteen(x):
    return -np.log(x**2 + 1) / np.e**x


def twentyOne(x):
    return np.e ** (x**2) - 2


def twentyTwo(x):
    return x**4 + np.cos(x) - np.log(x) ** 2


def plotFunction(f, a: float, b: float, title: str) -> None:
    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.plot([a, b], [f(a), f(b)], "r--", label="Initial Interval")


def goldenSearch(
    f: callable = twenty, a: float = -1, b: float = 3, tol: float = 1e-5
) -> float:
    ratio = (5**0.5 - 1) / 2
    c = b - ratio * (b - a)
    d = a + ratio * (b - a)

    plotFunction(f, a, b, "Golden Search Method Visualization")

    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - ratio * (b - a)
        d = a + ratio * (b - a)

        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.01)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return (a + b) / 2


def bisectionSearch(
    f: callable = twenty, a: float = -1, b: float = 3, tol: float = 1e-5
) -> float:
    plotFunction(f, a, b, "Bisection Search Method Visualization")
    L = b - a

    while L > tol:
        x1 = a + L / 4
        xm = (a + b) / 2
        x2 = b - L / 4

        if f(x1) > f(xm):
            if f(xm) < f(x2):
                a = x1
                b = x2
            else:
                a = xm
        else:
            b = xm
        L = b - a

        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.01)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()

    return (b + a) / 2


def main() -> None:
    with console.status("Optimizing...", spinner="point"):
        resGolden: float = f"{goldenSearch():.2f}"
        resBisection: float = f"{bisectionSearch():.2f}"
        scalarBounded: float = f"{optimize.minimize_scalar(f, bounds=(-1, 3)).x:.2f}"

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


data = [(twenty, -1, 3), (nineteen, 0, 3), (twentyOne, -1, 1), (twentyTwo, 0.5, 1.5)]

for f, a, b in data:
    resGolden: float = f"{goldenSearch(f, a, b):.2f}"
    resBisection: float = f"{bisectionSearch(f, a, b):.2f}"
    scalarBounded: float = f"{optimize.minimize_scalar(f, bounds=(a, b)).x:.2f}"

    console.print(f"Golden Section Method: {resGolden}")
    console.print(f"Bisection Method: {resBisection}")
    console.print(f"Bounded Scalar (from scipy): {scalarBounded}")
    console.print()
