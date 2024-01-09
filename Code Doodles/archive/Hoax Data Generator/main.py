from json import dumps
from os import makedirs, path
from random import choice, randint
from string import ascii_lowercase


def getRandomId(count):
    count = str(count)
    randomFiller = randint(100, 999)
    return int(count + str(randomFiller) + count)


def generateRandomName(length=5):
    lettes = ascii_lowercase
    return "".join([choice(lettes) for _ in range(length)]).capitalize()


def generateObjectValues(count):
    id = getRandomId(count)
    name = f"{generateRandomName(randint(5, 10))} {generateRandomName(randint(5, 10))}"
    email = f"{generateRandomName(randint(5, 10)).lower()}@gmail.com"
    age = randint(18, 60)
    return {"id": id, "name": name, "email": email, "age": age}


def generateObjects(count=0, numberOfObjects=9):
    res = []

    for _ in range(numberOfObjects):
        count += 1
        objectData = generateObjectValues(count)
        res.append(objectData)

    return res


def fillInFiles(files):
    currentDir = path.dirname(path.abspath(__file__))
    dataDir = path.join(currentDir, "data")
    makedirs(dataDir, exist_ok=True)
    for file in files:
        objectsData = generateObjects()
        intendedFilePath = path.join(dataDir, file)
        with open(intendedFilePath, "w") as f:
            jsonData = dumps(objectsData, indent=2)
            f.write(jsonData)


files = ["data.json", "result.json", "random.json", "objects.json", "testing.json"]
if __name__ == "__main__":
    fillInFiles(files)
