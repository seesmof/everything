# Import the combinations_with_replacement function from itertools module
from itertools import combinations_with_replacement

# Print an empty line
print("")

# Get input for N and convert it to an integer
n = int(input("Введіть N: "))

# Get input for K and convert it to an integer
k = int(input("Введіть K: "))

# Print an empty line
print("")

# Generate all possible combinations with replacement of integers 1 to N with length K
combinations = combinations_with_replacement(range(1, n+1), k)

# Initialize a count variable to keep track of the number of combinations
count = 0

# Loop through each combination
for combination in combinations:
    # Increment the count variable
    count += 1
    # Convert the combination to a string and join the individual integers into a single string
    combination_str = "".join(str(i) for i in combination)
    # Print the count and the combination as a string
    print(f"{count} - {combination_str}")

# Print the total number of combinations
print(f"\nЗагальна кількість комбінацій = {count}")

# Print an empty line
print("")
