import sympy as sp

t = sp.symbols("t")

# define the function
f = 5 * t + 3

# calculate a2 and b2
a2 = (1 / sp.pi) * sp.integrate(f * sp.cos(2 * t), (t, -sp.pi, sp.pi))
b2 = (1 / sp.pi) * sp.integrate(f * sp.sin(2 * t), (t, -sp.pi, sp.pi))

# print the difference a2 - b2
print(a2 - b2)
