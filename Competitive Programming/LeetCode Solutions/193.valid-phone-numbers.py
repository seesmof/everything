import re
from os import path
import inquirer
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
dataFolder = path.join(currentDir, "..", "data")
phoneNumbersFile = path.join(dataFolder, "193-phone-numbers.txt")

numbers = []

with open(phoneNumbersFile, "r") as file:
    for line in file:
        numbers.append(line.strip())

table = Table()
table.add_column("Status", style="bold", justify="right")
table.add_column("Number", style="cyan", no_wrap=True)


def validateNumber(number: str) -> bool:
    pattern = "^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
    result = re.match(pattern, number)
    return True if result else False


for number in numbers:
    validationResults = validateNumber(number)
    table.add_row("[green]Good[/]" if validationResults else "[red]Bad[/]", number)

console.print(table)

removeBadNumbersQuestion = [
    inquirer.Confirm(
        "removeBadNumbers",
        message="Would you like to remove bad numbers?",
        default=False,
    )
]
removeBadNumbersAnswer = inquirer.prompt(removeBadNumbersQuestion)
removeBadNumbers: bool = removeBadNumbersAnswer["removeBadNumbers"]

if removeBadNumbers:
    with open(phoneNumbersFile, "w") as file:
        for number in numbers:
            if validateNumber(number):
                file.write(number + "\n")
