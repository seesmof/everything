import random
import time

print()
sortingTimes = []
for _ in range(10):
    startTimer = time.time()
    arr = []
    for _ in range(1_000_000):
        arr.append(random.randint(1, 10**9))
    arr.sort()
    timeTaken = time.time() - startTimer
    sortingTimes.append(timeTaken)

averageSortingTime = sum(sortingTimes) / len(sortingTimes)
print(f"Average sorting time is {averageSortingTime:.2f} seconds")
sortingTimes = [round(time, 2) for time in sortingTimes]
print(f"\nAll sorting times: {', '.join(map(str, sortingTimes))}")
print()
