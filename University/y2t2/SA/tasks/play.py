from rich.console import Console
from rich.traceback import install

install()
console = Console()


arr = [
    [123, "Jesus loves you"],
    [321, "Jesus Christ is King of Kings"],
    [312, "God loves you all"],
]
proper = sorted(arr, key=lambda x: x[1])
console.print(arr, proper)
