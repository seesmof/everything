"""
(x-2)^2 

-1<x<3
"""

from rich.console import Console
from rich.traceback import install

install()
console = Console()


def findMax(x, y):
    maxIndex = np.argmax(y)
    return x[maxIndex], y[maxIndex]


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 1000)
y = (x - 2) ** 2

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("(x-2)^2")
plt.grid(True)

maxX, maxY = findMax(x, y)
console.print(f"Max: ({maxX}, {maxY})")

plt.scatter(maxX, maxY, color="red", marker="x", s=100)
plt.show()
