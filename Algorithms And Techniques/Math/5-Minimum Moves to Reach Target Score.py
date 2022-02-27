"""

2139. Minimum Moves to Reach Target Score
Medium

376

5

Add to List

Share
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.

 

Example 1:

Input: target = 5, maxDoubles = 0
Output: 4
Explanation: Keep incrementing by 1 until you reach target.
Example 2:

Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
Example 3:

Input: target = 10, maxDoubles = 4
Output: 4
Explanation: Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10
 

Constraints:

1 <= target <= 10^9
0 <= maxDoubles <= 100

"""

# Initially i didnt saw the constraints so i went on with dp
from functools import cache


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        @cache
        def go(num, doubles):
            if num == target:
                return 0

            if num*2 <= target and doubles > 0:
                op1 = 1 + go(num*2, doubles - 1)
                op2 = 1 + go(num+1, doubles)
                return min(op1, op2)
            return 1 + go(num+1, doubles)
        return go(1, maxDoubles)

# TLE


# Correct one
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        while target != 1:
            if target %2 == 0 and maxDoubles:
                count += 1
                target = target // 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    count += (target-1)
                    break
                else:
                    target -= 1
                    count += 1
        return count