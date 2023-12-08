import sympy as sp

# Define the symbols
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the differential equation
diff_eq = sp.Eq(y.diff(x) - (x * y / (x + 2)), 3 * sp.exp(x))

# Solve the differential equation
general_solution = sp.dsolve(diff_eq, y)

# Apply the initial condition y(-1) = 1/e
particular_solution = general_solution.subs(
    "C1", sp.solve(general_solution.rhs.subs(x, -1) - 1 / sp.exp(1), "C1")[0]
)

# Find y(0)
y_0 = particular_solution.rhs.subs(x, 0)

print(y_0)
