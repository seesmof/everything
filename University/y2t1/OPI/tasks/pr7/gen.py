import json
import random
import string


class RandomdData:
    @staticmethod
    def getString(length):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    @staticmethod
    def getInteger(rangeMin=1, rangeMax=100):
        return random.randint(rangeMin, rangeMax)


files = ["data.json", "result.json", "random.json", "objects.json"]

for file in files:
    objects = []
    count = 0
    for _ in range(9):
        count += 1
        id = int(str(count) + str(random.randint(100, 999)) + str(count))
        name = f"{RandomdData.getString(5).capitalize()} {RandomdData.getString(7).capitalize()}"
        email = f"{RandomdData.getString(5)+''.join(name.split()).lower()}@gmail.com"

        object = {
            "id": id,
            "name": name,
            "email": email,
            "age": RandomdData.getInteger(),
        }
        objects.append(object)
    count = 0
    json_data = json.dumps(objects)
    print()
    print(json_data)
    print()
    with open(file, "w") as outfile:
        outfile.write(json_data)
