"""
CountPathMaze
Given a 2D grid, find the number of ways to reach (n-1, n-1).
"""


def CountPathMaze(i, j):
    if i > len(maze) - 1 or j > len(maze):
        return 0
    if i == len(maze) - 1 and i == len(maze) - 1:
        return 1
    return CountPathMaze(i + 1, j) + CountPathMaze(i, j + 1)


maze = [[0 for i in range(3)] for j in range(3)]
print(CountPathMaze(0, 0))