n = int(input())
A, B, C = [], [], []
for _ in range(n):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
A, B, C = sorted(A), sorted(B), sorted(C)
subA = (A[n // 2] + A[n // 2 - 1]) // 2
subB = (B[n // 2] + B[n // 2 - 1]) // 2
subC = (C[n // 2] + C[n // 2 - 1]) // 2
res = 0
for a, b, c in zip(A, B, C):
    cur = abs(subA - a) + abs(subB - b) + abs(subC - c)
    res += cur
print(res)
