import os
import sys
from rich import print as pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)
