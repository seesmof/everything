"""
Kim Wexler is tired of working for Mesa Verde. Instead, she wants to solve the following problem.

Kim has two integers a and b. Help her to find any x such that 0≤x≤10**9 and the value of (a+x) AND (b+x) is minimized.

Here AND denotes the bitwise AND operator.

INPUT:
The first line contains a single integer t — the number of test cases. Then t test cases follow.
The first line of each test case contains two space-separated integers a and b.

OUTPUT:
For each test case, output a single integer — the answer to the problem. If there are several integers x such that 0≤x≤10**9 and the value of (a+x) AND (b+x) is minimized, you can output any of them.

TEST CASES (: symbolises input, > symbolises output):
:2
:1 11
> 1
:64 64
> 0
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(1)
