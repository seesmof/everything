import sympy as sp

x = sp.symbols('x')
f = 1/(x*sp.log(x)**2)

integral = sp.integrate(f, (x, 2, sp.oo))
print(integral)
