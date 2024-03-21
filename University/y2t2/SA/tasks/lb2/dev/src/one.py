"""
- Вивести всі коректні комбінації пар круглих дужок, які можна сформувати з n дужок, що закриваються і відкриваються. Наприклад, коректна комбінація (()()), некоректна (()))(. Кількість дужок задається користувачем
"""

import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def main() -> None:
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
        pass
    elif choice == options[1]:
        pass


if __name__ == "__main__":
    main()
