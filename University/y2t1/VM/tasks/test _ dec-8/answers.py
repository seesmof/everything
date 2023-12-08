import sympy as sp

n = sp.symbols("n")
term = 1 / sp.sqrt(2 * n + 1)

# Check if the terms decrease monotonically
prev_term = term.subs(n, 0)
for i in range(1, 100):
    next_term = term.subs(n, i)
    if next_term > prev_term:
        print("The series does not decrease monotonically.")
        break
    prev_term = next_term
else:
    print("The series decreases monotonically.")

# Check if the limit of the terms is zero
limit = sp.limit(term, n, sp.oo)
print("The limit of the terms as n approaches infinity is", limit)
