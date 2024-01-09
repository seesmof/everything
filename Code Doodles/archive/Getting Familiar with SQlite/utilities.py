def readFile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def createMembersDb(path: str, cursor):
    data = readFile(path)
    cursor.executescript(data)


def readMembersDb(cursor, consoleObject):
    cursor.execute("select * from members order by lastName")
    for row in cursor:
        consoleObject.print(row)
