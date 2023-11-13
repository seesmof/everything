"""
- Впорядкувати за не зростанням 5 чисел за 7 операцій порівняння.
- Є два відсортованих за не зростанням масиви A[1,N] і B[1,M]. Отримати відсортований за не зростанням масив C[1, N+M], що складається з елементів масивів A і B ("злити" разом масиви A і B).
"""


def sortFive(nums):
    def tournament(arr, i, j):
        if i == j:
            return [arr[i]]

        mid = (i + j) // 2
        left = tournament(arr, i, mid)
        right = tournament(arr, mid + 1, j)

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_nums = tournament(nums, 0, len(nums) - 1)[:5]
    return sorted_nums


def mergeArrays(A, B, C):
    # Є два відсортованих за не зростанням масиви A[1,N] і B[1,M]. Отримати відсортований за не зростанням масив C[1, N+M], що складається з елементів масивів A і B ("злити" разом масиви A і B).

    # if the first array is empty
    if not A:
        # we append our second array reversed, because the arrays are sorted in descending order
        return C + B[::-1]
    # if the second array is empty
    if not B:
        # same deal, appending the reversed first array to our resulting array
        return C + A[::-1]
    # if the last element, which is the smallest one, from first array is larger than the smallest element from second array
    if A[-1] > B[-1]:
        # we recursively merge them, but take out the last element from first array and append it to the resulting array
        return mergeArrays(A[:-1], B, C + [A[-1]])
    # if its not
    else:
        # we recursively merge our arrays, but now taking out the last element from second array and appending it to the resutling array
        return mergeArrays(A, B[:-1], C + [B[-1]])


def testSortFive():
    assert sortFive([5, 3, 8, 2, 1]) == [8, 5, 3, 2, 1]
    assert sortFive([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert sortFive([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert sortFive([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert sortFive([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert sortFive([22, 30, 94, 55, 71]) == [
        94,
        71,
        55,
        30,
        22,
    ]
    print("All tests have passed")


def testMergeArrays():
    assert mergeArrays([1, 3, 5, 7], [2, 4, 6, 8], []) == [8, 7, 6, 5, 4, 3, 2, 1]
    assert mergeArrays([1, 2, 3], [4, 5, 6], []) == [6, 5, 4, 3, 2, 1]
    assert mergeArrays([1, 1, 1], [1, 1, 1], []) == [1, 1, 1, 1, 1, 1]
    assert mergeArrays([1, 2, 3], [], []) == [3, 2, 1]
    assert mergeArrays([], [4, 5, 6], []) == [6, 5, 4]
    assert mergeArrays([20, 30, 90, 120, 240, 965], [], []) == [
        965,
        240,
        120,
        90,
        30,
        20,
    ]
    assert mergeArrays([], [], []) == []
    assert mergeArrays([10, 20, 30, 40, 50], [15, 25, 35, 45, 55], []) == [
        55,
        50,
        45,
        40,
        35,
        30,
        25,
        20,
        15,
        10,
    ]
    print("All tests have passed")


def menu():
    while True:
        print("\nMAIN MENU")
        print("1. Sort an array in descending order")
        print("2. Merge two arrays in descending order")
        print("3. Exit")
        choice = int(input(": "))

        if choice == 1:
            print("\nTASK ONE")
            print("1. Enter custom data")
            print("2. Run tests")
            print("3. Go back")
            localChoice = int(input(": "))
            print()

            if localChoice == 1:
                arr = list(map(int, input("Enter the array elements: ").split()))
                res = sortFive(arr)
                print(f"\nSorted array: {res}")
            elif localChoice == 2:
                testSortFive()

        elif choice == 2:
            print("\nTASK TWO")
            print("1. Enter custom data")
            print("2. Run tests")
            print("3. Go back")
            localChoice = int(input(": "))
            print()

            if localChoice == 1:
                A = list(
                    map(int, input("Enter the elements of the first array: ").split())
                )
                B = list(
                    map(int, input("Enter the elements of the second array: ").split())
                )
                res = mergeArrays(A, B, [])
                print(f"\nMerged arrays: {res}")
            elif localChoice == 2:
                testMergeArrays()

        else:
            break


if __name__ == "__main__":
    # menu()
    # testSortFive()
    numbers = [5, 3, 8, 1, 7]
    sorted_numbers = sortFive(numbers)
    print("Sorted numbers in non-increasing order:", sorted_numbers)
