from Archive.testing_imports import *


def solve(one: str, two: str) -> str:
    count = 1
    while True:
        trial = one[:count]
        console.print(trial)
        if trial not in one or trial not in two:
            return trial[:-1]
        else:
            count += 1


one, two = "ABCABC", "ABC"
res = solve(one, two)
console.print(f"{one}, {two}: {res}")
