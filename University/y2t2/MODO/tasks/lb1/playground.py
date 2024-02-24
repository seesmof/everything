"""
3x - 2y = -6

x=0
-2y=-6
y=3
(0,3)

y=0
3x=-6
x=-2
(-2,0)
"""

from matplotlib import pyplot as plt
import numpy as np


plt.title("Багатокутник рішень")
plt.xlabel("Вісь X₁")
plt.ylabel("Вісь X₂")

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xticks(np.arange(-5, 6, 1))
plt.yticks(np.arange(-5, 6, 1))

oneX2 = [0, 3]
oneX1 = [-2, 0]
plt.plot(oneX1, oneX2, color="red", label="3x1 - 2x2 = -6")

plt.grid()
plt.legend()
plt.show()
