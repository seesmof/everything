"""
- Вивести всі коректні комбінації пар круглих дужок, які можна сформувати з n дужок, що закриваються і відкриваються. Наприклад, коректна комбінація (()()), некоректна (()))(. Кількість дужок задається користувачем

Print all valid combinations of pairs of parentheses that can be formed from n closing and opening parentheses. For example, the correct combination is (()()), the incorrect combination is (()))(. The number of brackets is set by the user

Functional:
- function calls - defining anonymous functions based on calls to other functions
- recursion (i.e., it is forbidden to use loops, conditional statements, assignment statements, control statements except for return)

Imperative:
- ?
"""

import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def functional(n: int) -> None:
    pass


def imperative(n: int) -> None:
    pass


def main() -> None:
    bracketsNumber = inquirer.prompt(
        [
            inquirer.Text(
                "bracketsNumber",
                message="How many brackets would you like to use?",
                validate=lambda _, x: x != "" and x.isdigit(),
            )
        ]
    )["bracketsNumber"]

    options = [
        "Functional Programming",
        "Imperative Programming",
    ]
    choice = inquirer.prompt(
        [
            inquirer.List(
                "solution",
                message="Which solution would you like to use?",
                choices=options,
            )
        ]
    )["solution"]

    if choice == options[0]:
        functional(n=int(bracketsNumber))
    elif choice == options[1]:
        imperative(n=int(bracketsNumber))


if __name__ == "__main__":
    main()
