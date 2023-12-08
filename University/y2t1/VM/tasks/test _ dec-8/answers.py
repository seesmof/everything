from sympy import symbols, limit, oo

# Define the variable
n = symbols("n")

# Define the series sum
s_n = 2 * n / (n + 3)

# Calculate the limit as n approaches infinity
s = limit(s_n, n, oo)

print(s)
