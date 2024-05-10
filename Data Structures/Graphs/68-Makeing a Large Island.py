"""

URL: https://leetcode.com/problems/making-a-large-island/description/

827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 
Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 
Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 500
	grid[i][j] is either 0 or 1.

"""
from typing import List


class DisjointSetUnion:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.size = [1] * N
        self.comp = N

    def find(self, a: int) -> int:
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u: int, v: int) -> None:
        a, b = self.find(u), self.find(v)
        if a == b:
            return
        if b > a:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
        self.comp -= 1


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dsu = DisjointSetUnion(R * C)
        zeros = []

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    node = i * C + j
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                            new_node = nx * C + ny
                            dsu.union(node, new_node)
                else:
                    zeros.append([i, j])

        ans = -float('inf')
        for x, y in zeros:
            node = x * C + y
            parents = set()
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                    new_node = nx * C + ny
                    parents.add(dsu.find(new_node))
            total = 0
            for parent in parents:
                total += dsu.size[parent]
            ans = max(ans, total + 1)

        return ans