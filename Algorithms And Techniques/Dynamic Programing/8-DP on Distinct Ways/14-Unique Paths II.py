"""

63. Unique Paths II
Medium

3590

329

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""
from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[rows-1][cols-1] == 1:
            return 0

        @lru_cache(None)
        def dp(x, y):
            if x == rows - 1 and y == cols - 1:
                return 1
            if x == rows or y == cols:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            return dp(x+1, y) + dp(x, y+1)
        return dp(0, 0)
