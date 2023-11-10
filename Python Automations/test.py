class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [None] * capacity if capacity > 0 else [None]

    def get(self, i: int) -> int:
        return self.arr[i] if i <= len(self.arr) else -1

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n if i <= len(self.arr) else -1

    def pushback(self, n: int) -> None:
        if self.arr and self.arr[-1] != None:
            self.resize()
        self.arr.append(n)

    def popback(self) -> int:
        self.arr.pop() if len(self.arr) > 0 else -1

    def resize(self) -> None:
        newOne = []
        for _ in range(len(self.arr)):
            newOne.append(None)
        self.arr = self.arr + newOne

    def getSize(self) -> int:
        count = [el for el in self.arr if el != -1]
        return len(count)

    def getCapacity(self) -> int:
        return len(self.arr)


arr = DynamicArray(0)
print(arr.arr)
arr.pushback(5)
print(arr.arr)
arr.pushback(9)
arr.pushback(3)
arr.pushback(6)
arr.pushback(12)
arr.pushback(92)
print(arr.arr)
