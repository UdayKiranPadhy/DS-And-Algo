def Can_Place(x, y):
    """"""
    for i in range(n):
        if board[i][y] == "Q":
            return False
        if board[x][i] == "Q":
            return False
    count_for_diag = 1
    boundary_x = x
    boundary_y = y
    while boundary_x >= 0 and boundary_y >= 0:
        if boundary_x and boundary_y:
            if board[x - count_for_diag][y - count_for_diag] == "Q":
                return False
        boundary_x = x - count_for_diag
        boundary_y = y - count_for_diag
        count_for_diag += 1
    count_for_diag = 1
    boundary_x = x
    boundary_y = y
    while boundary_x <= n - 1 and boundary_y <= n - 1:
        if boundary_x < n - 1 and boundary_y < n - 1:
            if board[x + count_for_diag][y + count_for_diag] == "Q":
                return False
        boundary_y = y + count_for_diag
        boundary_x = x + count_for_diag
        count_for_diag += 1

    # Right Top to Left Bottom
    boundary_x = x
    boundary_y = y
    count_for_diag = 1
    while boundary_x <= n - 1 and boundary_y >= 0:
        if boundary_x < n - 1 and boundary_y:
            if board[x + count_for_diag][y - count_for_diag] == "Q":
                return False
        boundary_x = x + count_for_diag
        boundary_y = y - count_for_diag
        count_for_diag += 1
    boundary_x = x
    boundary_y = y
    count_for_diag = 1
    while boundary_x >= 0 and boundary_y <= n - 1:
        if boundary_x and boundary_y < n - 1:
            if board[x - count_for_diag][y + count_for_diag] == "Q":
                return False
        boundary_x = x - count_for_diag
        boundary_y = y + count_for_diag
        count_for_diag += 1
    return True


def display_board():
    """
    Prints Chess Board To the Standard Output
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                print(str(board[i][j]) + " |", end="")
            else:
                print(board[i][j] + " |", end="")
        print()
        for j in range(len(board)):
            print("__|", end="")
        print()


n = int(input())
board = [[0 for i in range(n)] for i in range(n)]
k = 0
iterator_column = [-1 for i in range(n)]
while k >= 0 and k <= n - 1:
    for i in range(iterator_column[k] + 1, len(board)):
        if (i == (len(board) - 1)) and (Can_Place(k, i) == False):
            iterator_column[k] = -1
            k -= 1
            board[k][iterator_column[k]] = 0
            break
        elif Can_Place(k, i):
            board[k][i] = "Q"
            iterator_column[k] = i
            k += 1
            break
    else:
        iterator_column[k] = -1
        k -= 1
        board[k][iterator_column[k]] = 0
display_board()


How to get all possible solution