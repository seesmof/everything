"""
x+y>=3
x+y=3

x=0
y=3

y=0
x=3


"""

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

# 3X1-2X2>=-6
oneX2 = [0, 3]
oneX1 = [-2, 0]
slope = (oneX2[1] - oneX2[0]) / (oneX1[1] - oneX1[0])
x = np.linspace(-6, 6, 100)
y = slope * (x - oneX1[0]) + oneX2[0]
plt.plot(x, y, color="red", label="3x1 - 2x2 >= -6")

# X1+X2>=3
twoX1 = np.linspace(-6, 6, 100)
twoX2 = 3 - twoX1
plt.plot(twoX1, twoX2, color="green", label="x1 + x2 >= 3")

# X1<=3
plt.axvline(x=3, color="blue", label="x1 <= 3")

# X2<=5
plt.axhline(y=5, color="orange", label="x2 <= 5")

plt.grid()
plt.legend()
plt.show()
