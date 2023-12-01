from math import sqrt


c = float(input())
for x in range(int(c)):
    if x**2 + sqrt(x) == c:
        print(float(x))
