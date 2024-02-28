"""
- Файл містить перелік повних адрес файлів (ім'я диску, список каталогів, ім'я файлу та розширення). Виділити з кожної адреси ім'я файлу, розширення та адресу першого каталогу. Перевірити для кожного файлу чи існує він. Вивести у файл, ім'я якого формується з імені початкового файлу додаванням постфіксу "str", перелік файлів, які існують на диску, згрупувавши їх за форматами та відсортувавши в алфавітному порядку за іменем файлів. Імена файлів виводити у форматі "/першийКаталог/.../ім'яФайлу/", сортуючи за розширенням та шляхом
- Продаж квитків у кінотеатр з можливістю переглядати сеанси, переглядати доступні та зайняті місця для перегляду заданого сеансу у відповідному залі, бронювання та звільнення місць. Інформація про нові сеанси може додаватися
"""

import json
import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich import box
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from os import path


def taskOne() -> None:
    currentDir = path.dirname(path.abspath(__file__))
    inputFilePath = path.join(currentDir, "..", "data", "files.txt")

    doUseReadyFile = inquirer.prompt(
        [
            inquirer.List(
                "choice",
                message="Would you like to use a predefined example or enter your own file path?",
                choices=["Predefined Example", "Own File Path"],
            )
        ]
    )["choice"]
    if doUseReadyFile == "Own File Path":
        inputFilePath = inquirer.prompt(
            [
                inquirer.Text(
                    "file path",
                    message="Enter your input file path",
                    validate=lambda _, x: "\\" in x or "/" in x and x != "",
                )
            ]
        )["file path"]

    outputFilePath = path.join(
        currentDir, "..", "data", inputFilePath.split("\\")[-1][:-4] + "_str.txt"
    )

    with open(inputFilePath, "r", encoding="utf-8") as f:
        fileNames = [line.strip() for line in f.readlines()]

    filesData = [
        {
            "name": file.split("\\")[-1].split(".")[0],
            "extension": file.split("\\")[-1].split(".")[-1],
            "first_dir": file.split("\\")[1],
            "does_exist": path.exists(file),
            "full_path": file,
        }
        for file in fileNames
    ]

    outputTable = Table(box=box.ROUNDED, title="All Files")
    outputTable.add_column("Index", justify="right", style="cyan", no_wrap=True)
    outputTable.add_column("File Name", style="green")
    outputTable.add_column("Extension", style="blue")
    outputTable.add_column("First Directory", style="magenta")
    outputTable.add_column("Does Exist", style="red", no_wrap=True, justify="right")
    for i, file in enumerate(filesData):
        outputTable.add_row(
            f"{i}",
            file["name"],
            file["extension"],
            file["first_dir"],
            "[green]Yes[/]" if file["does_exist"] else "No",
        )
    console.print("\n", outputTable, "\n")

    existingFiles = [file for file in filesData if file["does_exist"]]
    existingFiles.sort(key=lambda x: (x["extension"], x["full_path"], x["name"]))

    resultsTable = Table(box=box.ROUNDED, title="Existing Files")
    resultsTable.add_column("Index", justify="right", style="cyan", no_wrap=True)
    resultsTable.add_column("File Name", style="green")
    resultsTable.add_column("Extension", style="blue")
    resultsTable.add_column("File Path", style="yellow")
    for i, file in enumerate(existingFiles):
        resultsTable.add_row(
            f"{i}",
            file["name"],
            file["extension"],
            f"/{file['first_dir']}/.../{file['name']}.{file['extension']}",
        )
    console.print(resultsTable, "\n")

    with open(outputFilePath, "w", encoding="utf-8") as f:
        prevExtension = ""
        for file in existingFiles:
            curExtension = file["extension"]
            if curExtension != prevExtension:
                f.write(f"\n{curExtension.upper()}\n")
            f.write(f"{file['name']}.{file['extension']}\n")
            prevExtension = curExtension


def main() -> None:
    availableTasks = [
        "First - Reading file names from a file and checking if they exist",
        "Second - Cinema tickets seller simulation",
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
        taskOne()
    else:
        console.print("Sorry... No task here")


if __name__ == "__main__":
    main()
