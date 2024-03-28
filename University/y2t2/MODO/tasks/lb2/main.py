from rich.console import Console
from rich.traceback import install

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

install()
console = Console()


def f(x, epsilon=0.1):
    return -(np.log(x**2 + 1) / np.e**x)


def bisectionSearch(a=0, b=3, tol=1e-5):
    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


def goldenSearch(a=0, b=3, tol=1e-5):
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


with console.status("Оптимізуємо...", spinner="point"):
    res = f"{optimize.golden(f):.20f}"
    console.print(f"Відповідь: {res}")
    res = f"{optimize.golden(f):.20f}"
    console.print(f"Відповідь: {res}")

# plot the function
x = np.linspace(0, 3, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="(x-2)^2")
plt.title("Plot of (x-2)^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()
