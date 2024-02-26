from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


# Given values
X_2 = 5

# Equation: 3*X_1 - 2*X_2 = -6
# Solve for X_1
X_1 = (2 * X_2 - 6) / 3

console.print(X_1)

console.print(2 * X_1 + 2 * X_2)
