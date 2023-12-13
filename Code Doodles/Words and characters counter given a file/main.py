def retrieveFile(name):
    try:
        with open(name, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except:
        pass


def removeWhiteSpace(data):
    lines = data.split("\n")
    lines = [line for line in lines if line != ""]
    return lines, len(lines)


def countSymbols(lines):
    res = 0
    for line in lines:
        symbolsInLine = 0
        for char in line:
            symbolsInLine += 1
        res += symbolsInLine
    return res


def countWords(lines):
    res = 0
    for line in lines:
        wordsInLine = line.split(" ")
        res += len(wordsInLine)
    return res


# fileName = input("Enter file name: ")
fileName = "in.md"
fileContents = retrieveFile(fileName)
lines, linesCount = removeWhiteSpace(fileContents)
symbolsCount = countSymbols(lines)
wordsCount = countWords(lines)
print(
    f"\nThe provided text contains:\n  - {linesCount} lines\n  - {symbolsCount} symbols\n  - {wordsCount} words\n"
)
