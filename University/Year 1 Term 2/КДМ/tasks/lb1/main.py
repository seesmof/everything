# define a function to check if a pair is in the relation
def relation(a, b):
    return (2*a - b) % 3 == 0


print("")
# get input from user for both sets
A = set(map(int, input("Введіть елементи множини А: ").split()))
B = set(map(int, input("Введіть елементи множини B: ").split()))

# calculate and output the symmetric difference of A and B
symmetric_difference = set(A) ^ set(B)
print("\nA △ B:", symmetric_difference)

# calculate and output the binary relation matrix of A and B
matrix = [[int(relation(a, b)) for b in B] for a in A]
print("\nМатриця: ")
for row in matrix:
    print(row)
print("")
