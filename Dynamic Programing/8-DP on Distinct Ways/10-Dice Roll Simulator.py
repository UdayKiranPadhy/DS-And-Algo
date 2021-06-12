"""
Link:-https://leetcode.com/problems/dice-roll-simulation/
Date:-12/9/21

1223. Dice Roll Simulation
Hard

544

166

Add to List

Share
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30

Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
 
Example 4:
Input: n = 20, rollMax = [8,5,10,8,7,2]
Output: 822005673

Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15

"""


class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:

        @lru_cache(None)
        def Helper(n, last):
            if n == 0:
                return 1
            ways = 0
            for i in range(1, 7):
                if i == last[0]:
                    if last[1]-1 >= 0:
                        ways += Helper(n-1, (i, last[1]-1))
                    else:
                        continue
                else:
                    ways += Helper(n-1, (i, rollMax[i-1]-1))
            return ways % ((10**9) + 7)

        return Helper(n, (0, 0))


model = Solution()
print(model.dieSimulator(3, [1, 1, 1, 2, 2, 3]))
# 181
