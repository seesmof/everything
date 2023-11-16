class MinStack:
    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minValues[-1]:
            self.minValues.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


m = MinStack()
print(m.push(-2))
print(m.push(0))
print(m.push(-3))
print(m.getMin())
print(m.pop())
print(m.top())
print(m.getMin())
