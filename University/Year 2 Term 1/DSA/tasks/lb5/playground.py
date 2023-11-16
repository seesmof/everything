from collections import deque

container = deque()

container.appendleft(3)
container.appendleft(2)
container.appendleft(1)

container.popleft()
container.popleft()

print(list(container))
