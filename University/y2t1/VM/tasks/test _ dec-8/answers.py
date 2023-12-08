from sympy import symbols, diff, sin, cos, factorial

# Define the variable
x = symbols('x')

# Define the function
f = (sin(x)**2) / (cos(x)**2)

# Calculate the first and second derivatives at 0
f_prime_0 = diff(f, x).subs(x, 0)
f_double_prime_0 = diff(f, x, 2).subs(x, 0)

# Calculate the coefficients c_1 and c_2
c_1 = f_prime_0 / factorial(1)
c_2 = f_double_prime_0 / factorial(2)

print(c_1, c_2, c_1 + c_2)