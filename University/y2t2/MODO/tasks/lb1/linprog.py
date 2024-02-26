from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy.optimize import linprog

коефіцієнтиЦільовоїФункції = [-2, -2]

першеОбмеження = [[-3, 2], [-1, -1], [1, 0], [0, 1]]

векторРуху = [6, -3, 3, 5]

границіХ1 = (0, None)
границіХ2 = (0, None)

результат = linprog(
    коефіцієнтиЦільовоїФункції,
    A_ub=першеОбмеження,
    b_ub=векторРуху,
    bounds=[границіХ1, границіХ2],
    method="highs",
)

console.print(
    f"Оптимальне рішення: {результат.x}\nОптимальне значення: {-1 * результат.fun}"
)
