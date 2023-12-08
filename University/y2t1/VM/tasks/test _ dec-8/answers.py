import sympy as sp

x = sp.symbols("x")
f = sp.tan(x) ** 2

# calculate the first two derivatives
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)

# evaluate the derivatives at 0
c1 = f1.subs(x, 0)
c2 = f2.subs(x, 0) / 2  # divide by 2! to get the coefficient

print(c1 + c2)
