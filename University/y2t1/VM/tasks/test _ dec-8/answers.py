from sympy import symbols, limit, oo

n = symbols("n", integer=True)
x = symbols("x", real=True)
a = (x - 4) ** n / (n * 2**n)
RatioTest = abs(a.subs(n, n + 1) / a)
L = limit(RatioTest, n, oo)
a_left = a.subs(x, 4)
print(L)
print(a_left)
