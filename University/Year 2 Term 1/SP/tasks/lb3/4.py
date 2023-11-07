def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quickSort(greater) + equal + quickSort(less)


arr = [54, 93, 99, 100, 35]
print(arr)
print(quickSort(arr))
