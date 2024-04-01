Побудувати графік заданої функції на заданому інтервалі за допомогою пакету matplotlib. Розробити программну реалізацію процедури зменшення інтервалу пошуку з використанням обох вивчених методів одновимірного пошуку.

$(x-2)^2, [-1,3]$

- Написати й відлагодити програму, щореалізує етап встановлення меж інтервалу, що містить точку оптимуму, і процедуру зменшення інтервалу пошуку з використанням обох вивчених методів одновимірного пошуку.
- Вибрати початкову точку $x_0$ величину кроку $\Delta$ і встановити границі інтервалу, що містить точку оптимуму.
- Реалізувати попередній етап для величини кроку, що дорівнює $2\Delta$ і $\frac{\Delta}{2}$.
- Оцінити залежність ефективності пошуку граничних точок інтервалу від величини кроку $\Delta$. Всі наступні етапи завдання виконувати для величини кроку, обраної в попередньому пункті.
- Реалізувати процедуру одновимірного пошуку точки оптимуму заданої функції, використовуючи метод золотого перетину й метод розподілу інтервалу навпіл. У кожному випадку виконати задану викладачем кількість ітерацій.
- Порівняти результуючі інтервали пошуку, отримані за допомогою обох методів оптимізації з виключенням інтервалів.

---

- Сформульована мета роботи.
- Алгоритм і програми процедури встановлення границь інтервалу, що містить точку оптимуму, і процедур зменшення інтервалу пошуку з використанням методу розподілу інтервалу навпіл і методу золотого перетину,
- Результати роботи програм.
- Аналіз отриманих результатів і висновки

---

$-\frac{\ln(x^2+1)}{\epsilon^x}$

$\displaystyle-\frac{\ln(x^2+1)}{\epsilon^x}$

---

$\frac{ \sqrt{5}-1 }{ 2 }$

---

```
[a,b] - search interval
L = b-a

do
x1=a+L/4
xm=(a+b)/2
x2=b-L/4

if (f(x1)>f(xm))
	if (f(xm)<f(x2))
		a=x1
		b=x2
	else
a=xm
else
b=xm
L=b-a
while (L>e)
Print the middle of the interval and the value of the function at this point
```

---

from rich.console import Console
from rich.traceback import install

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

install()
console = Console()

def f(x):
return (x - 2) \*\* 2

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
ratio = (5\*_0.5 - 1) / 2
c = b - ratio _ (b - a)
d = a + ratio \* (b - a)

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

        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)

    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()
    return c

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

in bisection search they say the function is finding a zero of the function, not min. we need min. rework. heres also the algorithm they have as reference for bisection search:

[a,b] - search interval
L = b-a

do
x1=a+L/4
xm=(a+b)/2
x2=b-L/4

if (f(x1)>f(xm))
if (f(xm)<f(x2))
a=x1
b=x2
else
a=xm
else
b=xm
L=b-a
while (L>e)
Print the middle of the interval and the value of the function at this point
