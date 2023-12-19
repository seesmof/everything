from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md

install()
consoleTheme = Theme(
    {
        "warning": "bold yellow",
        "error": "bold red",
        "success": "bold green",
        "info": "bold blue",
    }
)
console = Console(theme=consoleTheme)


def prodArrExceptSelf(arr: [int]) -> [int]:
    res = []
    arraysWithoutSelves = {index: [] for index in range(len(arr))}

    for index, item in enumerate(arr):
        arrayWithoutCurrent = arr.copy()
        arrayWithoutCurrent.pop(index)
        arraysWithoutSelves[index] = arrayWithoutCurrent

    for index, arrayWithoutCurrent in arraysWithoutSelves.items():
        currentProduct = 1
        for number in arrayWithoutCurrent:
            currentProduct *= number
        res.append(currentProduct)

    return res


arr = [1, 2, 3, 4]
res = prodArrExceptSelf(arr)
console.print(res, res == [24, 12, 8, 6])

arr = [-1, 1, 0, -3, 3]
res = prodArrExceptSelf(arr)
console.print(res, res == [0, 0, 9, 0, 0])
