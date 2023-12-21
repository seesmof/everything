from rich.console import Console
import json

console = Console()


def solve(fileName):
    def loadLines():
        with open(fileName, "r") as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        return lines

    lines = loadLines()
    res = 0
    validDigits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def countLineValue(line):
        digits = []
        for c in line:
            digits.append(c) if c.isdigit() else None
        console.print(f"Digits: {digits}")
        value = int(digits[0] + digits[-1])
        return value

    for line in lines:
        value = countLineValue(line)
        console.print(f"Value: {value}")
        res += value

    return res


# availableFiles = ["input.txt", "hoax.txt"]
availableFiles = ["hoax.txt"]
results = []
for file in availableFiles:
    resultObject = {
        "file": file,
        "result": solve(file),
    }
    results.append(resultObject)
    console.log(f"Solved 'Trebuchet' for file {file}. Result: {resultObject['result']}")

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
