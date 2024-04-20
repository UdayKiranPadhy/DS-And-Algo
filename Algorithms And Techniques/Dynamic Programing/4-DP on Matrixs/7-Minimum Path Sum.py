"""

URL: https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150

64. Minimum Path Sum

AmazonMicrosoftGoogleGoldman SachsOracleGiven a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 
Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

 
Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 200
	0 <= grid[i][j] <= 200

"""
from functools import cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        @cache
        def dfs(x, y):
            if (x, y) == (R - 1, C - 1):
                return grid[x][y]
            res = float('inf')
            for dx, dy in [[1, 0], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    res = min(res, grid[x][y] + dfs(nx, ny))
            return res

        return dfs(0, 0)
