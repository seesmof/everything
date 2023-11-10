def solve(arr):
    requiredSize = len(set(arr))
    uniquesCounter = 0
    seens = {el: 0 for el in arr}

    print(seens)
    print(seens[arr[0]])

    for i in range(len(arr)):
        if seens[arr[i]] > 0:
            arr.pop(i)
        else:
            seens[arr[i]] += 1

    return uniquesCounter


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = solve(arr)
print(arr)
