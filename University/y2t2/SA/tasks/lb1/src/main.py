"""
- Файл містить перелік повних адрес файлів (ім'я диску, список каталогів, ім'я файлу та розширення). Виділити з кожної адреси ім'я файлу, розширення та адресу першого каталогу. Перевірити для кожного файлу чи існує він. Вивести у файл, ім'я якого формується з імені початкового файлу додаванням постфіксу "str", перелік файлів, які існують на диску, згрупувавши їх за форматами та відсортувавши в алфавітному порядку за іменем файлів. Імена файлів виводити у форматі "/першийКаталог/.../ім'яФайлу/", сортуючи за розширенням та шляхом
- Продаж квитків у кінотеатр з можливістю переглядати сеанси, переглядати доступні та зайняті місця для перегляду заданого сеансу у відповідному залі, бронювання та звільнення місць. Інформація про нові сеанси може додаватися
"""

import json
from rich.markdown import Markdown as md
from rich.table import Table
from rich import box
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from os import path

currentDir = path.dirname(path.abspath(__file__))
inputFilePath = path.join(currentDir, "..", "data", "files.txt")
rawJsonOutputPath = path.join(
    currentDir, "..", "data", inputFilePath.split("\\")[-1][:-4] + ".json"
)
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
with open(rawJsonOutputPath, "w", encoding="utf-8") as f:
    json.dump(filesData, f, indent=2, ensure_ascii=False)
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
console.print()
console.print(outputTable)
console.print()
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
console.print(resultsTable)
console.print()
prevExtension = ""
with open(outputFilePath, "w", encoding="utf-8") as f:
    for file in existingFiles:
        curExtension = file["extension"]
        f.write(f"\n{curExtension.upper()}\n") if prevExtension != curExtension else ""
        f.write(f"{file['name']}.{file['extension']}\n")
        prevExtension = curExtension
