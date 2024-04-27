"""

URL: https://leetcode.com/problems/shortest-bridge/description/

934. Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 
Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

 
Constraints:

	n == grid.length == grid[i].length
	2 <= n <= 100
	grid[i][j] is either 0 or 1.
	There are exactly two islands in grid.

"""

# Multi Source BFS


from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        q = deque()
        seen = set()

        def dfs(x, y):
            seen.add((x, y))
            q.append([x, y, 0])
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = x + dx
                ny = y + dy
                if (nx, ny) not in seen and 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                    dfs(nx, ny)

        found = False
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 and not found:
                    dfs(i, j)
                    found = True

        while q:
            x, y, steps = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = x + dx
                ny = y + dy
                if (nx, ny) not in seen and 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 1:
                        return steps
                    q.append([nx, ny, steps + 1])
                    seen.add((nx, ny))

        return 0
