import matplotlib.pyplot as plt
import numpy as np


def plot_bisection_search(f, a, b, tol):
    # Create a range of x values for plotting
    x = np.linspace(a, b, 1000)

    # Initialize the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)")
    plt.title("Bisection Search Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    # Plot the initial interval
    plt.plot([a, b], [f(a), f(b)], "r--", label="Initial Interval")

    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Plot the current interval
        plt.plot([a, b], [f(a), f(b)], "g--", label="Current Interval")
        plt.pause(0.1)  # Pause for a short time to allow the plot to update

    # Plot the final interval
    plt.plot([a, b], [f(a), f(b)], "b--", label="Final Interval")
    plt.show()


# Example usage
def f(x):
    return (x - 2) ** 2


plot_bisection_search(f, -1, 3, 1e-5)
