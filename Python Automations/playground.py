import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()

text = inquirer.text(message="Enter your username")
password = (inquirer.password(message="Please enter your password"),)
choice = inquirer.list_input("Public or private?", choices=["public", "private"])
correct = inquirer.confirm(
    "This will delete all your current labels and " "create a new ones. Continue?",
    default=False,
)
console.print(
    text,
    password,
    choice,
    correct,
)
