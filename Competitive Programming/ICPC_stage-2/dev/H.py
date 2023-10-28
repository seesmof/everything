"""

"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    smaller, larger = min(a, b), max(a, b)
    res = 0
    if a == b:
        res = a
    else:
        step = smaller // 2
    print(res)
