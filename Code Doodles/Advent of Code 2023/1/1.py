from rich.console import Console
import re
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

    def countLineValue(line):
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        value = int(digits[0] + digits[-1])
        return value

    for line in lines:
        value = countLineValue(line)
        res += value

    return res


availableFiles = ["input.txt", "hoax.txt"]
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
