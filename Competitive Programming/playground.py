import numpy as np
import matplotlib.pyplot as plt

# Define the range for x1 and x2
x1_range = np.linspace(-10, 10, 400)
x2_range = np.linspace(-10, 10, 400)

# Inequality
x2_ineq = (10 + 3 * x1_range) / 2
plt.plot(x1_range, x2_ineq, label="$-3x_1 +  2x_2 \leq  10$")

# Equation
x2_eq = (10 + 3 * x1_range) / 2
plt.plot(x1_range, x2_eq, label="$-3x_1 +  2x_2 =  10$")

# Derived equations
x1_derived = -10 / 3 - 2 / 3 * x2_range
x2_derived = 5 + 3 / 2 * x1_range
plt.plot(x1_derived, x2_range, label="$x_1 = -\frac{10}{3} - \frac{2}{3}x_2$")
plt.plot(x1_range, x2_derived, label="$x_2 =  5 + \frac{3}{2}x_1$")

# Plot settings
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("Plot of Inequalities and Equations")
plt.legend()
plt.grid(True)
plt.show()
