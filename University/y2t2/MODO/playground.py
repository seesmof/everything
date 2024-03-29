from scipy.optimize import minimize_scalar
import numpy as np
import matplotlib.pyplot as plt


# Define your function here
def f(x):
    return (x - 2) ** 2


# Use the golden section search method
result = minimize_scalar(f, method="golden")

print(result.x)  # The x-coordinate of the minimum

# plot the function
x = np.linspace(0, 3, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="(x-2)^2")
plt.title("Plot of (x-2)^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()
