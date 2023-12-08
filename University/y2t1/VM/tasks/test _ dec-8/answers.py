from sympy import symbols, limit, Abs, oo, Sum, factorial, S

# Define the variable and the sequence
x = symbols('x')
n = symbols('n', integer=True)
a_n = ((x-4)**n) / (n * 2**n)

# Calculate the ratio a_n / a_{n+1}
ratio = Abs(a_n / a_n.subs(n, n+1))

# Calculate the limit as n approaches infinity
R = limit(ratio, n, oo)

# Check the convergence at the left endpoint x = 4 - R
left_endpoint = 4 - R
series_at_left = a_n.subs(x, left_endpoint)
abs_series_at_left = Abs(a_n).subs(x, left_endpoint)

# Check if the series converges absolutely at the left endpoint
abs_convergence_at_left = Sum(abs_series_at_left, (n, 0, oo)).is_convergent()

# Check if the series converges conditionally at the left endpoint
conditional_convergence_at_left = Sum(series_at_left, (n, 0, oo)).is_convergent() and not abs_convergence_at_left

print(R, abs_convergence_at_left, conditional_convergence_at_left
)