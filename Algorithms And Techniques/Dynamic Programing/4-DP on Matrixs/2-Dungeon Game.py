"""
174. Dungeon Game
Hard

Share
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1
 

Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000

"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # cache the states
        @lru_cache(None)
        def dp(x, y):

            # FOR BASE CASE:
            if x == m-1 and y == n-1:
                # if last element is negative, then i've to be one more than its abs value
                # else if its positive, i've to be 1 because that's the least health i can have
                return max(1, -dungeon[x][y] + 1)

            # FOR THE CURRENT STATE I'M IN i.e., (x,y):

            # initially set answer to infinity for the (x,y) state that we'll find out
            ans = float("inf")

            # there are two moves possible,
            # so get answers from both the directions i.e., left and down
            # take the minimum answer from both of them in each direction

            # DOWN:
            if x+1 < m:
                ans = min(ans, dp(x+1, y))
            # LEFT:
            if y+1 < n:
                ans = min(ans, dp(x, y+1))

            # now you've the minimum answer required to go to left or down,
            # so we now calculate the total answer required by considering the state we are
            # currently in

            # since you are currently at a point, you'd have to add the negative of current value
            # to simulate the value i should have before hand to enter this current point
            # so negate the value and add (subracting basically)

            # for example if current value is -6 then i need 7 to come to this point
            # but if the current value is 8 then i virtually need 0 to come to this point

            ans += -dungeon[x][y]

            # again if your ans is +ve, then it means you'd need atleast *ans* health to enter
            # this current point
            # else if its negative, then it means you actually need no health to even enter because
            # of the positive orbs in the subsequent points.
            # so since i added the negative, i need to return the max of 1 and the ans at the end
            return max(1, ans)

        # start the recursion from top
        return dp(0, 0)
