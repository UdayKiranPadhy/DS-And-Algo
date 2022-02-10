"""

200. Number of Islands
Medium

12215

308

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

# Problem statement
# https://leetcode.com/problems/number-of-islands/

# Solution
# Classical graph-traversal algorithm. I prefer to use dfs,
# we need to start it from all points, and to change already
# visited cells to some new symbol, for example #.

# Complexity
# It is O(mn) for time and space

# Code

from itertools import product
from typing import List


class Solution:
    def numIslands(self, grid):
        m, n, cnt = len(grid), len(grid[0]), 0

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            for x, y in [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]:
                dfs(x, y)

        for i, j in product(range(m), range(n)):
            if grid[i][j] == '1':
                dfs(i, j)
                cnt += 1

        return cnt


# Code 2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        def dfs(i, j):
            if (i, j) in visited:
                return
            else:
                visited.add((i, j))
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                        if grid[nx][ny] == "1":
                            dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                else:
                    if grid[i][j] == "1":
                        count += 1
                        dfs(i, j)
        return count
