import time
import random

startTimer = time.time()
data = [random.randint(0, 1000) for _ in range(10000000)]
endTimer = time.time()
timeTaken = endTimer - startTimer
print(f"Time taken: {timeTaken:.2f} seconds")

start_time = time.time()
data.sort()
end_time = time.time()
elapsed_time = end_time - start_time

print(f"The sorting algorithm took {elapsed_time} seconds to execute.")
