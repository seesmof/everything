from fractions import Fraction
import math


def getC(n, k):
    return f"{n}!/({n-k}!*{k}!)"


p_0 = Fraction(math.comb(10, 4), math.comb(15, 4))
print(
    f"p0 = {getC(10, 4)} / {getC(15, 4)} = {math.comb(10, 4)}/{math.comb(15, 4)} = {p_0}"
)
p_1 = math.comb(5, 1) * Fraction(math.comb(10, 3), math.comb(15, 4))
print(
    f"p1 = {getC(5, 1)} * {getC(10, 3)} / {getC(15, 4)} = {math.comb(5, 1)}*{math.comb(10, 3)}/{math.comb(15, 4)} = {p_1}"
)
p_2 = Fraction(math.comb(5, 2) * math.comb(10, 2), math.comb(15, 4))
print(
    f"p2 = {getC(5, 2)} * {getC(10, 2)} / {getC(15, 4)} = {math.comb(5, 2)}*{math.comb(10, 2)}/{math.comb(15, 4)} = {p_2}"
)
p_3 = math.comb(5, 3) * Fraction(math.comb(10, 1), math.comb(15, 4))
print(
    f"p3 = {getC(5, 3)} * {getC(10, 1)} / {getC(15, 4)} = {math.comb(5, 3)}*{math.comb(10, 1)}/{math.comb(15, 4)} = {p_3}"
)
p_4 = Fraction(math.comb(5, 4), math.comb(15, 4))
print(
    f"p4 = {getC(5, 4)} / {getC(15, 4)} = {math.comb(5, 4)}/{math.comb(15, 4)} = {p_4}"
)

print()
print(p_0 + p_1 + p_2 + p_3 + p_4 == 1)
