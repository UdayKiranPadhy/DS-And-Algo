"""
576. Out of Boundary Paths

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of
the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to
move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.


https://leetcode.com/problems/out-of-boundary-paths/description/

"""
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i,j,move):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if not move:
                return 0
            left = dfs(i,j-1,move-1)
            right = dfs(i,j+1,move-1)
            up = dfs(i-1,j,move-1)
            down = dfs(i+1,j,move-1)
            return left + right + up + down
        return dfs(startRow,startColumn,maxMove) % (10**9 + 7)