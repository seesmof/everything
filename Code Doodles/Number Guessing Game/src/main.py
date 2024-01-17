"""
i dont even know what im doing at this point. God please help me, Jesus our Almighty God

so the task is to create a number guessing game - generate a random number, then prompt user to guess it and hint them if the guess is too high or too low

this reminded me of binary search so might wanna implement a game mode that will play itself and show the time its done in
"""

from random import randint
import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def getMaxNumber() -> int:
    q = [
        inquirer.Text(
            "maximum number",
            message="Enter max number, up to which you want to play",
            validate=lambda _, x: x.isnumeric(),
        ),
    ]
    a = inquirer.prompt(q)
    return int(a["maximum number"])


def getGuess() -> int:
    q = [
        inquirer.Text(
            "guess",
            message="Enter your guess",
            validate=lambda _, x: x.isnumeric(),
        )
    ]
    a = inquirer.prompt(q)
    return int(a["guess"])


maxNumber = getMaxNumber()
number = randint(1, maxNumber)
while True:
    g = getGuess()
    if g > number:
        console.print("Too high")
    elif g < number:
        console.print("Too low")
    else:
        console.print("Correct")
        break
