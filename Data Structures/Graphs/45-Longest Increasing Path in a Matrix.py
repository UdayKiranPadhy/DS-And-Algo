"""

329. Longest Increasing Path in a Matrix
Hard

4943

85

Add to List

Share
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1


https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


"""

# https://www.youtube.com/watch?v=wCc_nd-GiEc&ab_channel=NeetCode

from typing import List


# [[9,9,4],[6,6,8],[2,1,1]]
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        cache = {}

        def dfs(x, y):
            if (x, y) in cache and cache[(x, y)] != -float('inf'):
                return cache[(x, y)]
            result = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                    result = max(result, 1 + dfs(nx, ny))
            cache[(x, y)] = result
            return result

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        return max(cache.values())


model = Solution()
print(model.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))


# We regard

# a cell in the matrix as a node,
# a directed edge from node x to node y if x and y are adjacent and x's value < y's value
# Then a graph is formed.

# No cycles can exist in the graph, i.e. a DAG is formed.
#
# The problem becomes to get the longest path in the DAG.

# Topological sort can iterate the vertices of a DAG in the linear ordering.

# Using Kahn's algorithm(BFS) to implement topological sort while counting the levels can give us the longest chain of nodes in the DAG.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0

        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1

        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))

        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len
