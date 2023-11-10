class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [0] * capacity if capacity > 0 else []

    def get(self, i: int) -> int:
        return self.arr[i] if i <= len(self.arr) else -1

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n if i <= len(self.arr) else -1

    def pushback(self, n: int) -> None:
        self.arr.append(n)

    def popback(self) -> int:
        self.arr.pop() if len(self.arr) > 0 else -1

    def resize(self) -> None:
        self.arr[:] = self.arr * 2

    def getSize(self) -> int:
        return len(self.arr)

    def getCapacity(self) -> int:
        pass


arr = DynamicArray(5)
print(arr.arr)
arr.set(2, 5)
print(arr.arr)
arr.pushback(3)
arr.pushback(9)
arr.pushback(5)
arr.pushback(11)
print(arr.arr)
