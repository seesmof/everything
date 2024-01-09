from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install
import inquirer
from click_shell import shell

install()
console = Console()


@shell(prompt="> ")
def the_shell() -> None:
    console.print(
        "Welcome to my CLI project template.\nEnter 'help' for a list of commands."
    )


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
This is just a template for a CLI project.

Here is a list of available commands:

- help: Show this help message
- quit: Exit the shell
"""
        )
    )


@the_shell.command()
def meow() -> None:
    catQuestions = [
        inquirer.List(
            "type",
            message="What type of meow do you want?",
            choices=["meow", "purr", "woof", "furr"],
        ),
        inquirer.Text(
            "name",
            message="What is your name?",
            default="Stranger",
            validate=lambda _, x: x != "",
        ),
    ]
    catAnswers = inquirer.prompt(catQuestions)
    console.print(f"Meow, {catAnswers['name']} is a {catAnswers['type']}!")


if __name__ == "__main__":
    the_shell()
