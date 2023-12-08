import sympy as sp

t = sp.symbols("t")
f = 5 * t + 3

a_2 = sp.integrate(f * sp.cos(2 * t), (t, -sp.pi, sp.pi)) / sp.pi
b_2 = sp.integrate(f * sp.sin(2 * t), (t, -sp.pi, sp.pi)) / sp.pi

diff = a_2 - b_2
print(diff)
