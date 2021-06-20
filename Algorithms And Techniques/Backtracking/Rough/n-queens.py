# def display_board(l):
#     """
#     Prints Chess Board To the Standard Output
#     """
#     for i in range(len(l)):
#         for j in range(len(l[i])):
#             if l[i][j] == 1:
#                 print(str(l[i][j]), end=" ")
#             else:
#                 print(l[i][j], end=" ")
#         print()


# def place_queen(board, position):
#     """
#     Parameters Board,Position
#     Position = Tuple Format
#     Board 8x8 list
#     Places the Queen in the Given Position And Marks All attacking sqaures as 1 in board
#     """

#     # Placeing the Queen in the Position
#     x, y = position
#     board[x][y] = "Q"

#     # Horizontal Traversal
#     for i in range(8):
#         if board[i][y] != "Q":
#             board[i][y] = 1

#     # Vertical Traversal
#     for j in range(8):
#         if board[x][j] != "Q":
#             board[x][j] = 1

#     # Left Top to Right Bottom Traversal
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x >= 0 and boundary_y >= 0:
#         if boundary_x and boundary_y:
#             if board[x - count_for_diag][y - count_for_diag] != "Q":
#                 board[x - count_for_diag][y - count_for_diag] = 1
#         boundary_x = x - count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x <= 7 and boundary_y <= 7:
#         if boundary_x < 7 and boundary_y < 7:
#             if board[x + count_for_diag][y + count_for_diag] != "Q":
#                 board[x + count_for_diag][y + count_for_diag] = 1
#         boundary_y = y + count_for_diag
#         boundary_x = x + count_for_diag
#         count_for_diag += 1

#     # Right Top to Left Bottom
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x <= 7 and boundary_y >= 0:
#         if boundary_x < 7 and boundary_y:
#             if board[x + count_for_diag][y - count_for_diag] != "Q":
#                 board[x + count_for_diag][y - count_for_diag] = 1
#         boundary_x = x + count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x >= 0 and boundary_y <= 7:
#         if boundary_x and boundary_y < 7:
#             if board[x - count_for_diag][y + count_for_diag] != "Q":
#                 board[x - count_for_diag][y + count_for_diag] = 1
#         boundary_x = x - count_for_diag
#         boundary_y = y + count_for_diag
#         count_for_diag += 1
#     return board


# def Can_Place(board, position):
#     x, y = position
#     for i in range(8):
#         if board[i][y] == "Q":
#             return False
#         if board[x][i] == "Q":
#             return False
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x >= 0 and boundary_y >= 0:
#         if boundary_x and boundary_y:
#             if board[x - count_for_diag][y - count_for_diag] == "Q":
#                 return False
#         boundary_x = x - count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x <= 7 and boundary_y <= 7:
#         if boundary_x < 7 and boundary_y < 7:
#             if board[x + count_for_diag][y + count_for_diag] == "Q":
#                 return False
#         boundary_y = y + count_for_diag
#         boundary_x = x + count_for_diag
#         count_for_diag += 1

#     # Right Top to Left Bottom
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x <= 7 and boundary_y >= 0:
#         if boundary_x < 7 and boundary_y:
#             if board[x + count_for_diag][y - count_for_diag] == "Q":
#                 return False
#         boundary_x = x + count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x >= 0 and boundary_y <= 7:
#         if boundary_x and boundary_y < 7:
#             if board[x - count_for_diag][y + count_for_diag] == "Q":
#                 return False
#         boundary_x = x - count_for_diag
#         boundary_y = y + count_for_diag
#         count_for_diag += 1
#     return True


# board = [[0 for i in range(8)] for i in range(8)]
# queen_placemeant = []
# left = 0
# down = 0
# while len(queen_placemeant) != 8:
#     for i in range(8):
#         for j in range(8):
#             if board[i][j] == 0:
#                 if Can_Place(board, (i, j)):
#                     queen_placemeant.append([i,j])
#                     place_queen(board, (i, j))
# display_board(board)

"""
At this point of time I understood That normal for loops wont be able to give me the answer,
Recursion is the way to go.
"""


def n_queen(board, queen_placemeants):
    if len(queen_placemeants) == 8:
        return queen_placemeants
    else:
        for i in range(8):
            for j in range(8):
                if Can_Place(board, (i, j)):
                    queen_placemeants.append([i, j])
                    return n_queen(place_queen(board.copy(), (i, j)), queen_placemeants)


"""
Failure With Recursion

"""

# import pdb

# pdb.set_trace()
# board = [[0 for i in range(8)] for i in range(8)]
# queen_placemeant = []
# print(n_queen(board, queen_placemeant))

"""
Came to know that it can be done through recursion , but i dont know how to do that,
3rd try reading the question , we dont need to place 1 in the attacking square , we just need to check 
if already a queen is placed in the horizontal , veritcal and diagonal positions or not.
"""

# board = [[0 for i in range(8)] for i in range(8)]
# queen_placemeant = []

# def Can_Place(board, position):
#     x, y = position
#     for i in range(8):
#         if board[i][y] == "Q":
#             return False
#         if board[x][i] == "Q":
#             return False
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x >= 0 and boundary_y >= 0:
#         if boundary_x and boundary_y:
#             if board[x - count_for_diag][y - count_for_diag] == "Q":
#                 return False
#         boundary_x = x - count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     count_for_diag = 1
#     boundary_x = x
#     boundary_y = y
#     while boundary_x <= 7 and boundary_y <= 7:
#         if boundary_x < 7 and boundary_y < 7:
#             if board[x + count_for_diag][y + count_for_diag] == "Q":
#                 return False
#         boundary_y = y + count_for_diag
#         boundary_x = x + count_for_diag
#         count_for_diag += 1

#     # Right Top to Left Bottom
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x <= 7 and boundary_y >= 0:
#         if boundary_x < 7 and boundary_y:
#             if board[x + count_for_diag][y - count_for_diag] == "Q":
#                 return False
#         boundary_x = x + count_for_diag
#         boundary_y = y - count_for_diag
#         count_for_diag += 1
#     boundary_x = x
#     boundary_y = y
#     count_for_diag = 1
#     while boundary_x >= 0 and boundary_y <= 7:
#         if boundary_x and boundary_y < 7:
#             if board[x - count_for_diag][y + count_for_diag] == "Q":
#                 return False
#         boundary_x = x - count_for_diag
#         boundary_y = y + count_for_diag
#         count_for_diag += 1
#     return True

# count = 0

# while count < 8:
#     board[0][count] = "Q"
#     for i in range(8):
#         if Can_Place(board,(1,i)):
#             board[1][j] = "Q"


"""
Last Trail before Seein gthe Answer, We only need to increment any one of the following either row or column
"""
# n = 8

"""
*--------------------------GIVE UP---------------------* Uday Kiran
"""

"""
Solve
This function is the main entry in solving the N queens problem. It takes
the partially filled board and the column we are trying to place queen in.
It will return a boolean value which indicates whether or not we found a
successful arrangement starting from this configuration.

Base case: if there are no more queens to place, we have successed

Otherwise, we find a safe row in this column, place a queen at (row,col)
recursively call Solve starting at the next column using this new board
configuration. If that Solve call fails, we remove that queen from (row,col)
and try again with the next safe row within the column. If we have tried all
rows in this column and haven't found a solution, we return false from this
invocation, which will force backtracking from this unsolvable configuration.

The starting call to Solve has an empty board and places a queen in col 0:
Solve(board, 0);

Procedue :-

Bool Solve ( board ,col):
    if col >= board.numcol() : retun True

    for (rowToTry = 0 ; rowToTry <board.numrow(); rowToTry++):
        if (IsSafe(board,rowToTry,col)):
            PlaceQueen(Board,rowToTry,col)
            if Solve(board , col+1) : return True
            RemoveQueen(board , rowToTry,col)
        
    return False



GG
"""


def Can_Place(board, position):
    x, y = position
    for i in range(n):
        if board[i][y] == 1:
            return False
        if board[x][i] == 1:
            return False
    count_for_diag = 1
    boundary_x = x
    boundary_y = y
    while boundary_x >= 0 and boundary_y >= 0:
        if boundary_x and boundary_y:
            if board[x - count_for_diag][y - count_for_diag] == 1:
                return False
        boundary_x = x - count_for_diag
        boundary_y = y - count_for_diag
        count_for_diag += 1
    count_for_diag = 1
    boundary_x = x
    boundary_y = y
    while boundary_x <= 7 and boundary_y <= 7:
        if boundary_x < 7 and boundary_y < 7:
            if board[x + count_for_diag][y + count_for_diag] == 1:
                return False
        boundary_y = y + count_for_diag
        boundary_x = x + count_for_diag
        count_for_diag += 1

    # Right Top to Left Bottom
    boundary_x = x
    boundary_y = y
    count_for_diag = 1
    while boundary_x <= 7 and boundary_y >= 0:
        if boundary_x < 7 and boundary_y:
            if board[x + count_for_diag][y - count_for_diag] == 1:
                return False
        boundary_x = x + count_for_diag
        boundary_y = y - count_for_diag
        count_for_diag += 1
    boundary_x = x
    boundary_y = y
    count_for_diag = 1
    while boundary_x >= 0 and boundary_y <= 7:
        if boundary_x and boundary_y < 7:
            if board[x - count_for_diag][y + count_for_diag] == 1:
                return False
        boundary_x = x - count_for_diag
        boundary_y = y + count_for_diag
        count_for_diag += 1
    return True


def place_queen(board, position):
    x, y = position
    board[x][y] = 1


def RemoveQueen(board, position):
    x, y = position
    board[x][y] = 0


def Solve(board, column=0):
    if column > len(board[0]):
        return True

    for i in range(len(board)):
        if Can_Place(board, (i, column)):
            place_queen(board, (i, column))
            if Solve(board, column + 1):
                return True
            RemoveQueen(board, (i, column))

    return False


n = 7
board = [[0 for i in range(n)] for j in range(n)]
print(Solve(board))
