"""
- Впорядкувати за не зростанням 5 чисел за 7 операцій порівняння.
- Є два відсортованих за не зростанням масиви A[1,N] і B[1,M]. Отримати відсортований за не зростанням масив C[1, N+M], що складається з елементів масивів A і B ("злити" разом масиви A і B).

- Sort 5 numbers in non-increasing order for 7 comparison operations.
- There are two arrays A[1,N] and B[1,M] sorted in ascending order. Get a non ascending sorted array C[1, N+M], consisting of the elements of arrays A and B ("merge" arrays A and B together).
"""


def selectionSort(arr):
    # Base case: if the list is empty or contains a single element, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Find the minimum element in the list
        minValue = min(arr)
        minIndex = arr.index(minValue)
        # Swap the minimum element with the first element
        arr[0], arr[minIndex] = arr[minIndex], arr[0]
        # Recursively sort the rest of the list
        return selectionSort(arr[1:]) + [arr[0]]


def testSelectionSort():
    assert selectionSort([5, 3, 8, 2, 1]) == [8, 5, 3, 2, 1]
    assert selectionSort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert selectionSort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert selectionSort([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert selectionSort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert selectionSort([22, 30, 94, 55, 71]) == [
        94,
        71,
        55,
        30,
        22,
    ]
    print("All tests have passed")


def merge_recursive(A, B, C):
    if not A:
        return C + B
    if not B:
        return C + A
    if A[0] < B[0]:
        return merge_recursive(A[1:], B, C + [A[0]])
    else:
        return merge_recursive(A, B[1:], C + [B[0]])


# Test the function
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
C = []
print(merge_recursive(A, B, C))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
