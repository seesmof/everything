from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

weekStatus = "Чисельник"

dailyMessage = f"""
### Слава Ісусу Христу

- Тиждень - **{weekStatus}**
"""

console.print()
console.print(md(dailyMessage))
console.print()
