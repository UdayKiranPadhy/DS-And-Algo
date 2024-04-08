"""


174. Dungeon Game Hard Topics Companies Uber Amazon The demons had captured the princess and imprisoned her in the
bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was
initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering
these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health
(represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room
where the princess is imprisoned.



Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]] Output: 7 Explanation: The initial health of the knight must be at
least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN. Example 2:

Input: dungeon = [[0]]
Output: 1


"""
from typing import List


# Solution 1 TLE
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        N = len(dungeon)
        M = len(dungeon[0])
        directions = [[1, 0], [0, 1]]

        def dfs(limit, x, y) -> bool:
            if limit > 0 and (x, y) == (N - 1, M - 1):
                return True
            if limit <= 0:
                return False
            result = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and limit + dungeon[nx][ny] > 0:
                    result |= dfs(limit + dungeon[nx][ny], nx, ny)
            return result

        low, high = 0, 14
        while low < high:
            mid = low + (high - low) // 2

            if dfs(mid + dungeon[0][0], 0, 0):
                high = mid
            else:
                low = mid + 1
        return low


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])

        def dfs(x, y):
            if (x, y) == (M - 1, N - 1):
                return max(1, -dungeon[x][y]+1)

            total = float('inf')
            if y + 1 < N:
                total = min(total, dfs(x, y + 1))
            if x + 1 < M:
                total = min(total, dfs(x + 1, y))

            total += -dungeon[x][y]

            return max(1, total)

        return dfs(0, 0)


model = Solution()
print(model.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
