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

tasks: dict[str, callable] = {
    "First - Bracket Pairs": taskOne.main,
    "Second - Words Counter": taskTwo.main,
}


def main() -> None:
    availableTasks: list[str] = list(tasks.keys())
    selectedTask: str = inquirer.prompt(
        [
            inquirer.List(
                "task",
                message="Which task would you like to look at?",
                choices=availableTasks,
            )
        ]
    )["task"]

    tasks[selectedTask]()


if __name__ == "__main__":
    main()
