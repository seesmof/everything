num_runs = int(input("How many times do you want to run the program? "))

for i in range(num_runs):
    a = int(input("Enter integer A: "))
    b = int(input("Enter integer B: "))
    result = a % b
    print("A % B = ", result)
