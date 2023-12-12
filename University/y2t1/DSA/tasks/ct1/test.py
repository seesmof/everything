class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return int((key * ((5**0.5 - 1) / 2) % 1) * self.size)

    def insert(self, key, value):
        self.table[self.hash(key)].append((key, value))

    def delete(self, key):
        chain = self.table[self.hash(key)]
        for i, kv in enumerate(chain):
            if kv[0] == key:
                del chain[i]
                return True
        return False

    def search(self, key):
        chain = self.table[self.hash(key)]
        for kv in chain:
            if kv[0] == key:
                return kv[1]
        return None

    def display(self):
        for cell in range(self.size):
            print(f"Cell {cell}")
            for keyValuePair in self.table[cell]:
                print(f"  K: {keyValuePair[0]}, V: {keyValuePair[1]}")
        print()


def getKeyFromString(data):
    return sum(ord(c) for c in data)


table = HashTable()
table.display()

name, value = "Andrew", 20
key = getKeyFromString(name)
table.insert(key, value)
table.display()
