from rich.console import Console
from rich.traceback import install

install()
console = Console()


def f(x):
    return (x - 2) ** 2


a = -1
b = 3
c = a

while (b - a) > 1e-5:
    c = (a + b) / 2
    if f(c) == 0:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(c)
