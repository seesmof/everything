# Step 1: Ask the user for a number
try:
    num = int(input("Enter a positive integer to generate a multiplication table: "))
except ValueError:
    print("ERROR: Please enter a valid positive integer.")
else:
    # Step 2: Validate the input
    if num <= 0:
        print("ERROR: Please enter a positive integer.")
    else:
        # Step 3: Generate a multiplication table for the number up to 10
        print(f"\nMultiplication table for {num}:")
        for i in range(1, 9 + 1):
            print(f"{num} * {i} = {num * i}")
