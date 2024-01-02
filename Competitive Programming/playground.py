from rich.console import Console
from rich.traceback import install

install()
console = Console()


def mergeAlternately(one: str, two: str):
    res = ""
    while one or two:
        if one:
            res += one[0]
            one = one[1:]
        if two:
            res += two[0]
            two = two[1:]
    return res


one, two = "ab", "pqrs"
res = mergeAlternately(one, two)
console.print(res)
