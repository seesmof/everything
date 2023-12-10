FILE_PATH = (
    "D:/code/everything/Code Doodles/Replacing Words and moscovian Letters/config.json"
)
import json


def printExisting():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        data = data["replacements"]
    print()
    for replacement in data:
        print(f"{replacement['repA']} - {replacement['repB']}")
    print()


printExisting()


def addNewOne(repA, repB):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    new_replacement = {
        "active": True,
        "case": "Override",
        "repA": repA,
        "repB": repB,
        "type": "Swap",
    }

    for replacement in data["replacements"]:
        if replacement["repA"] == repA:
            print("🤔 That replacement already exists\n")
            return

    data["replacements"].append(new_replacement)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    printExisting()


def removeExisting(repA):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    for index, replacement in enumerate(data["replacements"]):
        if replacement["repA"] == repA:
            data["replacements"].pop(index)
            break

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    printExisting()


newOne = "росію"
replaceWith = "московію"

addNewOne(newOne, replaceWith)

removeThis = "путіна"
# removeExisting(removeThis)
