def root(n):
    nums = list(map(int, str(n)))
    sum = 0
    for i in nums:
        sum += i
    return sum


n = int(input())
res = root(n)
if res < 10:
    print(res)
else:
    print(root(res))
