"""
Date:- 09/7/21
Source :- https://leetcode.com/problems/matchsticks-to-square/

Matchsticks to Square
Medium

You are given an integer array matchsticks where matchsticks[i] is the length of the ith 
matchstick. You want to use all the matchsticks to make one square. You should not 
break any stick, but you can link them up, and each matchstick must be used exactly 
one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks 
with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8

"""


# Using Bitmasking DP
from functools import lru_cache


def MatchSticks(sticks):
    target, rem = divmod(sum(sticks), 4)
    if rem != 0:
        return False
    if max(sticks) > target:
        return False

    N = len(sticks)

    # Find sets which are possible
    masks = []

    @lru_cache(None)
    def go(index, t, mask):
        if t == target:
            masks.append(mask)
            return
        if t > target or index >= N:
            return
        for i in range(N):
            if (mask & (1 << i) == 0):
                go(index+1, t+sticks[i], mask | (1 << i))

    go(0, 0, 0)
    # Find Which 4 set combines to form a square and uses all the numbers

    target_path = (1 << len(sticks)) - 1

    def path_finder(i, p):
        nonlocal res, masks

        if res:
            return None

        if p == target_path:
            res = True
            return None

        if i == len(masks):
            return None

        if not masks[i] & p:
            path_finder(i+1, p | masks[i])
        path_finder(i+1, p)

    res = False
    path_finder(0, 0)
    return res


print(MatchSticks([6, 6, 6, 6, 4, 2, 2]))
