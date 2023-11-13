"""
- Дано дві цілочисельних таблиці A[1:10] і В[1:15]. Розробити алгоритм і написати програму, яка перевіряє, чи є ці таблиці схожими. Дві таблиці називаються схожими, якщо збігаються множини чисел, що зустрічаються в цих таблицях
- Є два відсортованих за не зростанням масиви A[1,N] і B[1,M]. Отримати відсортований за не зростанням масив C[1, N+M], що складається з елементів масивів A і B ("злити" разом масиви A і B).
"""


def compareTables(A: [[int]], B: [[int]]):
    # Дано дві цілочисельних таблиці A[1:10] і В[1:15]. Розробити алгоритм і написати програму, яка перевіряє, чи є ці таблиці схожими. Дві таблиці називаються схожими, якщо збігаються множини чисел, що зустрічаються в цих таблицях

    def isSubList(childList, parentList):
        # taking each element in a child list
        for element in childList:
            # checking if the element is not in parent list
            if element not in parentList:
                # if so, return false
                return False
        # if we didnt return in the loop, then the child list is a sublist of parent list
        return True

    # taking two tables and iterating over each one
    for subList, List in zip(A, B):
        # checking if current sublist is not a sublist of list from larger table
        if not isSubList(subList, List):
            # if not, return false
            return False
    # if we exited out of the loop and didnt return False, this means that each list in table one is a sublist of table two
    return True


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


def testCompareTables():
    assert (
        compareTables(
            [
                [1, 2, 3],
                [3, 2, 1],
                [4, 4, 4],
            ],
            [[1, 3, 4, 1, 2, 6], [3, 5, 8, 1, 2, 2], [4, 7, 5, 9, 4, 4]],
        )
        == True
    ), "Test 1 failed"
    assert (
        compareTables(
            [
                [1, 2],
                [3, 4],
            ],
            [
                [1, 1, 1],
                [2, 2, 2],
            ],
        )
        == False
    ), "Test 2 failed"
    assert (
        compareTables(
            [
                [9],
                [4],
            ],
            [
                [3, 2, 9],
                [4, 1, 1],
            ],
        )
        == True
    ), "Test 3 failed"
    assert (
        compareTables(
            [
                [9, 6, 2, 1],
                [6, 1, 7, 8],
                [5, 3, 7, 1],
            ],
            [
                [8, 3, 6, 1, 5, 9],
                [1, 6, 9, 2, 5, 6],
                [2, 9, 5, 7, 2, 7],
            ],
        )
        == False
    ), "Test 4 failed"
    print("All tests have passed")


def testMergeArrays():
    assert mergeArrays([1, 3, 5, 7], [2, 4, 6, 8], []) == [
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
    ], "Test 1 failed"
    assert mergeArrays([1, 2, 3], [4, 5, 6], []) == [6, 5, 4, 3, 2, 1], "Test 2 failed"
    assert mergeArrays([1, 1, 1], [1, 1, 1], []) == [1, 1, 1, 1, 1, 1], "Test 3 failed"
    assert mergeArrays([1, 2, 3], [], []) == [3, 2, 1], "Test 4 failed"
    assert mergeArrays([], [4, 5, 6], []) == [6, 5, 4], "Test 5 failed"
    assert mergeArrays([20, 30, 90, 120, 240, 965], [], []) == [
        965,
        240,
        120,
        90,
        30,
        20,
    ], "Test 6 failed"
    assert mergeArrays([], [], []) == [], "Test 7 failed"
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
    ], "Test 8 failed"
    print("All tests have passed")


import random


def menu():
    while True:
        print("\nMAIN MENU")
        print("1. Determine if tables are similar")
        print("2. Merge two arrays in descending order")
        print("3. Exit")
        choice = int(input(": "))

        if choice == 1:
            print("\nTASK ONE")
            print("1. Generate random tables")
            print("2. Run tests")
            print("3. Go back")
            localChoice = int(input(": "))
            print()

            if localChoice == 1:
                tableA = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
                tableB = [[random.randint(1, 9) for _ in range(8)] for _ in range(8)]
                res = compareTables(tableA, tableB)

                print()
                for array in tableA:
                    for element in array:
                        print(element, end=" ")
                    print()

                print()
                for array in tableB:
                    for element in array:
                        print(element, end=" ")
                    print()

                print(f"\nThe two tables are {'similar' if res else 'not similar'}")
            elif localChoice == 2:
                testCompareTables()

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
    menu()
