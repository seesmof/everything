"""
- Вивести всі коректні комбінації пар круглих дужок, які можна сформувати з n дужок, що закриваються і відкриваються. Наприклад, коректна комбінація (()()), некоректна (()))(. Кількість дужок задається користувачем
- Визначити кількість слів у тексті, що зберігається у файлі, та довжину найкоротшого слова. Слова відділяються одне від одного не тільки пробілами, але й будь-якими знаками пунктуації
"""

import inquirer
from rich.console import Console
from rich.traceback import install

import one as taskOne
import two as taskTwo

install()
console = Console()


def main() -> None:
    availableTasks = [
        "First - Bracket Pairs",
        "Second - Words Counter",
    ]
    selectedTask = inquirer.prompt(
        [
            inquirer.List(
                "task",
                message="Which task would you like to look at?",
                choices=availableTasks,
            )
        ]
    )["task"]

    if selectedTask == availableTasks[0]:
        taskOne.main()
    elif selectedTask == availableTasks[1]:
        taskTwo.main()


if __name__ == "__main__":
    main()
