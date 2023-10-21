import math

C1 = -1/4
C2 = 2
x = 1

y_1 = C1 * math.exp(x) + C2 * math.exp(2*x) + x**2 - 3/2*x - 3/4
print(y_1)
