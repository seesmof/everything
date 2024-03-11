import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


issue = inquirer.prompt(
    [
        inquirer.Text("issue", message="Whats going on", validate=lambda _, x: x != ""),
    ]
)["issue"]

if issue == "Dont turn on":
    if 
if issue == "Turn on but no screen":
    pass
if issue == "Cant press turn on button":
    pass
if issue == "Blue screen":
    pass
if issue == "Program crash":
    pass
if issue == "Cant update":
    pass
if issue == "Cant install":
    pass
if issue == "Cant open":
    pass
if issue == "No internet":
    pass
if issue == "Making noise":
    pass
if issue == "Freezing / Working slow":
    pass
