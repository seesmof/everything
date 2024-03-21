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
        if openCount == closeCount == n:
            console.print("".join(currentCombination))
            return

        if openCount < n:
            currentCombination.append("(")
            helper(openCount + 1, closeCount, currentCombination)
            currentCombination.pop()

        if closeCount < openCount:
            currentCombination.append(")")
            helper(openCount, closeCount + 1, currentCombination)
            currentCombination.pop()

    helper(0, 0, [])


def imperative(n: int) -> None:
    stack: list[tuple[str, int, int]] = []
    stack.append(("", 0, 0))

    while stack:
        currentCombination, openCount, closeCount = stack.pop()

        if openCount == closeCount == n:
            console.print(currentCombination)
            continue

        if openCount < n:
            stack.append((currentCombination + "(", openCount + 1, closeCount))

        if closeCount < openCount:
            stack.append((currentCombination + ")", openCount, closeCount + 1))


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

    bracketsNumber = inquirer.prompt(
        [
            inquirer.Text(
                "number of brackets",
                message="How many brackets would you like to use?",
                validate=lambda _, x: x != "" and x.isdigit() and int(x) > 0,
            )
        ]
    )["number of brackets"]
    bracketsNumber = int(bracketsNumber)

    console.print(f"\nAll possible bracket pairs for {bracketsNumber} bracket pairs:")
    if choice == options[0]:
        functional(n=bracketsNumber)
    elif choice == options[1]:
        imperative(n=bracketsNumber)


if __name__ == "__main__":
    main()
