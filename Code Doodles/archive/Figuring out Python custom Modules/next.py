import main
from rich.console import Console
from rich.traceback import install
install()
console=Console()

res=main.formFibonacci(100)
console.print(res)