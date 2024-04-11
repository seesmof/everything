"""
- Вивести всі коректні комбінації пар круглих дужок, які можна сформувати з n дужок, що закриваються і відкриваються. Наприклад, коректна комбінація (()()), некоректна (()))(. Кількість дужок задається користувачем

Print all valid combinations of pairs of parentheses that can be formed from n closing and opening parentheses. For example, the correct combination is (()()), the incorrect combination is (()))(. The number of brackets is set by the user

Functional:
- function calls - defining anonymous functions based on calls to other functions
- recursion (i.e., it is forbidden to use loops, conditional statements, assignment statements, control statements except for return)
"""

import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def functional(n: int) -> None:
    def helper(openCount: int, closeCount: int, currentCombination: list[str]):
        def printCombination() -> None:
            console.print("".join(currentCombination))

        def addLeftParenthesis() -> None:
            currentCombination.append("(")
            helper(openCount + 1, closeCount, currentCombination)
            currentCombination.pop()

        def addRightParenthesis() -> None:
            currentCombination.append(")")
            helper(openCount, closeCount + 1, currentCombination)
            currentCombination.pop()

        (openCount == closeCount == n and printCombination()) or (
            openCount < n and addLeftParenthesis()
        ) or (closeCount < openCount and addRightParenthesis())

    helper(0, 0, [])


def imperative(n: int) -> None:
    stack: list[tuple[str, int, int]] = []
    stack.append(("", 0, 0))

    while stack:
        currentCombination, openCount, closeCount = stack.pop()

        def printCombination() -> None:
            console.print(currentCombination)

        def addLeftParenthesis() -> None:
            stack.append((currentCombination + "(", openCount + 1, closeCount))

        def addRightParenthesis() -> None:
            stack.append((currentCombination + ")", openCount, closeCount + 1))

        (openCount == closeCount == n and printCombination()) or (
            openCount < n and addLeftParenthesis()
        ) or (closeCount < openCount and addRightParenthesis())


def main() -> None:
    tasks = {"Functional Programming": functional, "Imperative Programming": imperative}
    choice = inquirer.prompt(
        [
            inquirer.List(
                "solution",
                message="Which solution would you like to use?",
                choices=list(tasks.keys()),
            )
        ]
    )["solution"]

    bracketsNumber = inquirer.prompt(
        [
            inquirer.Text(
                "number of brackets",
                message="How many bracket pairs would you like to have?",
                validate=lambda _, x: x != "" and x.isdigit() and int(x) > 0,
            )
        ]
    )["number of brackets"]
    bracketsNumber = int(bracketsNumber)

    console.print(f"\nAll possible bracket pairs for {bracketsNumber} bracket pairs:")
    tasks[choice](n=bracketsNumber)


if __name__ == "__main__":
    main()
