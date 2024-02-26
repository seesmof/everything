"""
x+y>=3
x+y=3

x=0
y=3

y=0
x=3
"""


def getSlope(X1: list[int], X2: list[int]) -> float:
    return (X2[1] - X2[0]) / (X1[1] - X1[0])


from matplotlib import pyplot as plt
import numpy as np


plt.title("Багатокутник рішень")
plt.xlabel("Вісь X₁")
plt.ylabel("Вісь X₂")

# defining the visible area of our plot
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# making grid more dense markign every 1 unit
plt.xticks(np.arange(-6, 7, 1))
plt.yticks(np.arange(-6, 7, 1))

# marking X and Y axis with black lines
plt.axhline(color="black")
plt.axvline(color="black")

# 3X1 - 2X2 > =-6
oneX2 = [0, 3]
oneX1 = [-2, 0]
slope = getSlope(X1=oneX1, X2=oneX2)
x = np.linspace(-6, 6, 100)
y = slope * (x - oneX1[0]) + oneX2[0]
plt.plot(x, y, color="red", label="3x1 - 2x2 >= -6")

# X1 + X2 >= 3
twoX1 = [0, 3]
twoX2 = [3, 0]
slope = getSlope(X1=twoX1, X2=twoX2)
x = np.linspace(-6, 6, 100)
y = slope * (x - twoX1[0]) + twoX2[0]
plt.plot(x, y, color="green", label="x1 + x2 >= 3")

# X1 <= 3
plt.axvline(x=3, color="blue", label="x1 <= 3")

# X2 <= 5
plt.axhline(y=5, color="lime", label="x2 <= 5")

# C(2,2)
vectorStart = [0, 2]
vectorEnd = [0, 2]
plt.plot(vectorStart, vectorEnd, color="purple", label="C(2,2)")

# The Line
theLineX1 = [0, 2]
theLineX2 = [2, 0]
theLineSlope = getSlope(X1=theLineX1, X2=theLineX2)
x = np.linspace(-6, 6, 100)
y = theLineSlope * (x - theLineX1[0]) + theLineX2[0]
plt.plot(x, y, color="orange", label="Фінальна лінія")

plt.grid()
plt.legend()
plt.show()
