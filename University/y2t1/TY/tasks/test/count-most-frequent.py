ARR = []


from collections import Counter


def result(arr):
    counts = Counter(arr)
    return sorted(set(arr), key=lambda x: (-counts[x], x))


res = result(ARR)
print(res[0])
