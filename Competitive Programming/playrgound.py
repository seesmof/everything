def isValidSudoku(board: [[str]]) -> bool:
    def validateLine(line: [str]):
        line = [el for el in line if el != "."]
        return True if len(line) == len(set(line)) else False

    for row in board:
        if not validateLine(row):
            return False

    columns = []
    for currentIndex in range(len(board)):
        columnHolder = []
        for row in board:
            for index, element in enumerate(row):
                if index == currentIndex:
                    columnHolder.append(element)
        columns.append(columnHolder)
    for col in columns:
        if not validateLine(col):
            return False

    squares = {}
    for i in range(3):
        for j in range(3):
            squares[(i, j)] = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            identifier = (i // 3, j // 3)
            squares[identifier].append(board[i][j])
    for _, value in squares.items():
        print(value)
        if not validateLine(value):
            return False

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
res = isValidSudoku(board)
print(res)

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
res = isValidSudoku(board)
print(res)
