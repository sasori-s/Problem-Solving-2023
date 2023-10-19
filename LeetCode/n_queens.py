import copy

def isSafe(board, row, col, n):
    dup_col = col
    dup_row = row

    while col >= 0 and row >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
        
    col = dup_col
    row = dup_row

    while col >= 0:
        if board[row][col] == 'Q':
            return False
        
        col -= 1
        
    col = dup_col
    row = dup_row
        
    while col >= 0 and row < n:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    # print('passed')

    return True


def findPath(board, n, col, result):
    if col == n:
        result.append(copy.deepcopy(board))
        return

    for row in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            findPath(board, n, col + 1, result)
            board[row][col] = "."



if __name__ == '__main__':
    n = 4
    board = [["...."]for i in range(n)]

    print(board[1][2])

    col = 0
    result = []

    # findPath(board, n, col, result)
    # print(result)
    # print(board)
