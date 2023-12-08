import sympy as sp

n = sp.symbols("n")
a_n = (2**n + 3) / (3**n + 2)
L = sp.limit(a_n ** (1 / n), n, sp.oo)

print(L)
