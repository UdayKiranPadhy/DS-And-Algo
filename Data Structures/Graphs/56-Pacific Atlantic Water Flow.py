"""

https://leetcode.com/problems/pacific-atlantic-water-flow/

417. Pacific Atlantic Water Flow
Medium

7218

1432

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105


"""
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]):
        R = len(heights)
        C = len(heights[0])

        if not heights or not heights[0]: return []

        def bfs(starts):
            queue = deque(starts)
            seen = set(starts)
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and heights[nx][ny] >= heights[x][y] and (nx, ny) not in seen:
                        queue.append((nx, ny))
                        seen.add((nx, ny))
            return seen

        pacific = [(0, i) for i in range(R)] + [(i, 0) for i in range(1, C)]
        atlantic = [(R - 1, i) for i in range(R)] + [(i, C - 1) for i in range(R - 1)]

        return bfs(pacific) & bfs(atlantic)


class Solution:
    def pacificAtlantic(self, M):
        if not M or not M[0]: return []

        m, n = len(M[0]), len(M)

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited and M[dx][dy] >= M[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))

            return visited

        pacific = [(0, i) for i in range(m)] + [(i, 0) for i in range(1, n)]
        atlantic = [(n - 1, i) for i in range(m)] + [(i, m - 1) for i in range(n - 1)]

        return bfs(pacific) & bfs(atlantic)
