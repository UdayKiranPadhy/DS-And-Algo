"""

Max Area of Island

Solution
You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.


"""

# Solution
"""
Idea:
So we can just use a simple iteration through the grid and look for 
islands. When we find an island, we can use a recursive helper 
function (trav) to sum up all the connected pieces of land and 
return the total land mass of the island.

As we traverse over the island, we can replace the 1s with 0s to 
prevent "finding" the same land twice. We can also keep track of 
the largest island found so far (ans), and after the grid has been 
fully traversed, we can return ans.

Time Complexity: O(N * M) where N and M are the lengths of the 
sides of the grid
Space Complexity: O(L) where L is the size of the largest island, 
representing the maximum recursion stack
or O(N * M + L) if we create an N * M matrix in order to not modify the input
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(node):
            total = 1
            x, y = node
            grid[x][y] = 0
            for dx, dy in directions:
                if 0 <= x + dx < M and 0 <= y + dy < N and grid[x + dx][y + dy] == 1:
                    total += dfs((x + dx, y + dy))
            return total

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    area = max(area, dfs((i, j)))

        return area
