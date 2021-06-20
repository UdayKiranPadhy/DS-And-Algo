# def display_maze():
#     for i in range(len(A)):
#         for j in range(len(A)):
#             print(A[i][j], end="  ")
#         print()
# A = [
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 0, 1, 0],
#     [1, 0, 0, 1, 1],
#     [1, 0, 1, 1, 1],
# ]
# current_point = [0, 0]
# k = 0
# iterator_column = 0
# while current_point != [len(A) - 1, len(A) - 1]:
#     for i in range(iterator_column, len(A)):
#         if A[k][i] != 0 and A[k][i]!="R":
#             A[k][i] = "R"
#             k += 1
#             iterator_column = i
#             display_maze()
#             print()
#             break
#         else:
#             k -= 1
#             iterator_column += 1
#             display_maze()
#             print()
#             break


maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1],
]


def rat_maze(i, j):
    if (i < 0) or (j < 0):
        return False
    if (i > len(maze) - 1) or (j > len(maze) - 1):
        return False
    if (i == len(maze)) and (j == len(maze[0])):
        return True
    for i in range(len(maze)):
        if maze[i][j] == 1:
            maze[i][j] = "R"
            if rat_maze(i+1,j):
                return True
            if rat_maze(i, j + 1):
                return True
            maze[i][j] = 1
    return False
print(rat_maze(0, 0))
