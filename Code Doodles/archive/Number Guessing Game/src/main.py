"""
i dont even know what im doing at this point. God please help me, Jesus our Almighty God

so the task is to create a number guessing game - generate a random number, then prompt user to guess it and hint them if the guess is too high or too low

this reminded me of binary search so might wanna implement a game mode that will play itself and show the time its done in
"""

from random import randint
from time import sleep
import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def getMaxNumber() -> int:
    question = [
        inquirer.Text(
            "maximum number",
            message="Enter max number, up to which you want to play",
            validate=lambda _, x: x.isnumeric(),
        ),
    ]
    answer = inquirer.prompt(question)
    return int(answer["maximum number"])


def getGuess() -> int:
    question = [
        inquirer.Text(
            "guess",
            message="Enter your guess",
            validate=lambda _, x: x.isnumeric(),
        )
    ]
    answer = inquirer.prompt(question)
    return int(answer["guess"])


def getAutoMode() -> bool:
    question = [
        inquirer.Confirm(
            "auto",
            message="Enable auto mode? The game will play itself until it guesses correctly",
        )
    ]
    answer = inquirer.prompt(question)
    return answer["auto"]


def main():
    maxNumber = getMaxNumber()
    number = randint(1, maxNumber)
    autoMode = getAutoMode()
    if not autoMode:
        while True:
            guess = getGuess()
            if guess > number:
                console.print("Too high")
            elif guess < number:
                console.print("Too low")
            else:
                console.print("Correct")
                break
    else:
        low, high = 1, maxNumber

        with console.status("Guessing..."):
            while low <= high:
                sleep(0.1)
                guess = (low + high) // 2
                console.print(f"Is it {guess}?")
                if guess == number:
                    break
                elif guess > number:
                    high = guess - 1
                else:
                    low = guess + 1

        console.print(f"The number was {number}" if guess == number else "You lose")


if __name__ == "__main__":
    main()
