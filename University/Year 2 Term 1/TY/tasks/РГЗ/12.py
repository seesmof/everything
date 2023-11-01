import matplotlib.pyplot as plt
import numpy as np


def F(x):
    if x < 0:
        return 0
    elif x >= 0 and x < 2:
        return x - 0.25 * x**2
    else:
        return 1


def f(x):
    if x < 0 or x >= 2:
        return 0
    elif x >= 0 and x < 2:
        return 1 - 0.5 * x


# Create an array of x values from -1 to 3
x = np.linspace(-1, 3, 400)

# Vectorize the functions
F_vec = np.vectorize(F)
f_vec = np.vectorize(f)

# Create y values for each function
y_F = F_vec(x)
y_f = f_vec(x)

# Create two subplots
fig, axs = plt.subplots(2)

# Plot F(x)
axs[0].plot(x, y_F, label="F(x)")
axs[0].set_title("Distribution function F(x)")
axs[0].legend()

# Plot f(x)
axs[1].plot(x, y_f, label="f(x)", color="orange")
axs[1].set_title("Probability density function f(x)")
axs[1].legend()

# Display the plots
plt.tight_layout()
plt.show()
