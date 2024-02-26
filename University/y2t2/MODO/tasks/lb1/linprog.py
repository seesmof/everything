from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy.optimize import linprog

коефіцієнти_цільової_функції = [-2, -2]

коефіцієнти_нерівностей_до = [[-3, 2], [-1, -1], [1, 0], [0, 1]]
коефіцієнти_нерівностей_після = [6, -3, 3, 5]

границі_Х1 = (0, None)
границі_Х2 = (0, None)

with console.status("Оптимізуємо...", spinner="point"):
    результат = linprog(
        c=коефіцієнти_цільової_функції,
        A_ub=коефіцієнти_нерівностей_до,
        b_ub=коефіцієнти_нерівностей_після,
        bounds=[границі_Х1, границі_Х2],
    )

вихідні_дані = f"""
{результат}

Значення цільової функції: {-результат.fun}
Значення X1: {результат.x[0]}
Значення X2: {результат.x[1]}
"""
console.print(вихідні_дані)

поточна_тека = path.dirname(path.abspath(__file__))
шлях_до_файлу = path.join(поточна_тека, "output.txt")
with open(шлях_до_файлу, "w", encoding="utf-8") as f:
    f.write(вихідні_дані)
