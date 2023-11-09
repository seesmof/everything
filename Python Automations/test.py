def solve(arr):
    res = arr[:]
    el = res[-1]
    index = -1
    if el != 9:
        digit = el + 1
        res[index] = digit
    else:
        while el == 9:
            el = arr[index]
            el += 1
            digit, high = el % 10, el // 10
            res[index] = digit
            res[index - 1] = high
            index -= 1
        if res[0] == 9:
            res[0] = 0
            res.insert(0, 1)
    return res


arr = [1, 2, 3]
res = solve(arr)
print(res)
arr = [9, 9, 9]
res = solve(arr)
print(res)
