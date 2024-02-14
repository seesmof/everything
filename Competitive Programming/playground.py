from typing import List
from functools import cache
import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()

A, B, C = 0, 0, 0
n = int(input())
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))
    A += a
    B += b
    C += c
A, B, C = A // n, B // n, C // n
res = 0
for a, b, c in arr:
    res += abs(a - A) + abs(b - B) + abs(c - C)
print(res)
