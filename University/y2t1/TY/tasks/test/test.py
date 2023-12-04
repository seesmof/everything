"""
Неперервна двовимірна випадкова величина (X,Y) задана щільністю розроділ f(x,y) = {x+y, (x,y) є D; 0, (x,y) !є D}, де область D - квадрат, обмежений прямими x=0, x=1, y=0, y=1. Знайти числові характеристики (X,Y).
"""

import sympy as sp

x, y = sp.symbols("x y")
f = x + y

# Сподівання
E_X = sp.integrate(x * f, (x, 0, 1))
E_Y = sp.integrate(y * f, (y, 0, 1))

# Відхилення
Var_X = sp.integrate((x - E_X) ** 2 * f, (x, 0, 1))
Var_Y = sp.integrate((y - E_Y) ** 2 * f, (y, 0, 1))

# Коваріантність
Cov_XY = sp.integrate((x - E_X) * (y - E_Y) * f, (x, 0, 1), (y, 0, 1))

print(E_X)
print(E_Y)
print(Var_X)
print(Var_Y)
print(Cov_XY)
