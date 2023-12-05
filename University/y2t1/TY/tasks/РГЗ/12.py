from fractions import Fraction


def F(x):
    if x < 0:
        return 0
    elif 0 <= x < 2:
        return x - 0.25 * x**2
    else:
        return 1


a = 0
b = 0.5
P = F(b) - F(a)
print(f"F(a) = {F(a)}")
print(f"F(b) = {F(b)} or {Fraction(F(b))}")
print(f"F(b) - F(a) = {F(b) - F(a)} or {Fraction(F(b) - F(a))}")
print("P(X∈[a;b]) =", Fraction(P))
