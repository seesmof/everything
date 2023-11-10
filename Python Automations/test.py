def solve(arr):
    requiredSize = len(set(arr))
    uniquesCounter = 0
    seens = {el: 0 for el in arr}
    print(seens)

    return uniquesCounter


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = solve(arr)
print(arr)
