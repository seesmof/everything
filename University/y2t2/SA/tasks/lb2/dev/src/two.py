"""
- Визначити кількість слів у тексті, що зберігається у файлі, та довжину найкоротшого слова. Слова відділяються одне від одного не тільки пробілами, але й будь-якими знаками пунктуації

Determine the number of words in the text stored in the file and the length of the shortest word. Words are separated from each other not only by spaces, but also by any punctuation marks. you have to use functions like map, filter, reduce, ...
"""

import inquirer
from os import path
from functools import reduce
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def functional(filePath: str) -> tuple[int, int]:
    with open(filePath, "r", encoding="utf-8") as file:
        text = file.read()

    punctuation = '!@#$%^&*()_+{}|:"<>?`~'
    table = str.maketrans("", "", punctuation)

    words = text.translate(table).split()
    wordsCount = len(words)

    shortestWordLength = reduce(
        lambda acc, word: min(acc, len(word)), words, float("inf")
    )

    return wordsCount, shortestWordLength


def main() -> None:
    currentDir: str = path.dirname(path.abspath(__file__))
    filePath: str = path.join(currentDir, "..", "data", "input.txt")

    choices = [
        "Use provided file",
        "Enter path for my own",
    ]
    decision = inquirer.prompt(
        [
            inquirer.List(
                "choose",
                message="Which path would you like to use?",
                choices=choices,
            )
        ]
    )["choose"]

    if decision == choices[1]:
        filePath = inquirer.prompt(
            [
                inquirer.Text(
                    "path",
                    message="Enter full path to your file",
                    validate=lambda _, x: path.exists(x) and path.isfile(x),
                )
            ]
        )["path"]
        console.print()

    wordsCount, shortestWordLength = functional(filePath)
    console.print(f"Number of words: {wordsCount}")
    console.print(f"Length of shortest word: {shortestWordLength}")


if __name__ == "__main__":
    main()
