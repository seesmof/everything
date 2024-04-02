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


def goldenSearch(f, a: float = -1, b: float = 3, tol: float = 1e-5):
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

        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return (a + b) / 2


def bisectionSearch(f, a: float = -1, b: float = 3, tol: float = 1e-5):
    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)")
    plt.title("Bisection Search Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.plot([a, b], [f(a), f(b)], "r--", label="Initial Interval")

    while abs(b - a) >= tol:
        x1 = a + (b - a) / 3
        x2 = b - (b - a) / 3

        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return (a + b) / 2


data = [(twenty, -1, 3), (nineteen, 0, 3), (twentyOne, -1, 1), (twentyTwo, 0.5, 1.5)]

for f, a, b in data:
    resGolden: float = f"{goldenSearch(f, a, b):.2f}"
    resBisection: float = f"{bisectionSearch(f, a, b):.2f}"
    scalarBounded: float = f"{optimize.minimize_scalar(f, bounds=(a, b)).x:.2f}"

    console.print(f"Golden Section Method: {resGolden}")
    console.print(f"Bisection Method: {resBisection}")
    console.print(f"Bounded Scalar (from scipy): {scalarBounded}")
    console.print()
