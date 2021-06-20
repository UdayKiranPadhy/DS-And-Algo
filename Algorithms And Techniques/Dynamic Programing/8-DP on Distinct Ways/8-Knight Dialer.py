"""
Link :- https://leetcode.com/problems/knight-dialer/
Date :- 11/06/21

935. Knight Dialer
Medium

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:

Input: n = 3
Output: 46

Example 4:

Input: n = 4
Output: 104

Example 5:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
 
Constraints:

1 <= n <= 5000

"""

# My Trails Did not successed , 0 test cases Passes ,fk

class Solution:
    def knightDialer(self, n: int) -> int:
        steps = [[-2, -1], [-2, 1], [-1, -2],
                 [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

        def helper(row, column, n):
            if n == 0:
                return 1
            numbers = 0
            for dx , dy in steps:
                if ( ( (row + dx) <= 3 and (column + dy) <= 2 ) and ( (row+dx,column+dy) != (3,0) ) and ( (row+dx,column+dy) != (3,2) ) ):
                    numbers += helper(row+dx, column+dy, n-1)
            return numbers

        ways = 0
        for i in range(0, 4):
            for j in range(0, 3):
                if (i,j) != (3,0) and (i,j) != (3,2):
                    ways += helper(i, j, n)
        return ways



class Solution:
    def knightDialer(self, N: int) -> int:
        from functools import lru_cache
        
        neighbours = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(onKey, stepsLeft):
            if stepsLeft == 0:
                return 1
            elif stepsLeft == 1:
                return len(neighbours[onKey])
            else:
                tRes = 0
                for nextKey in neighbours[onKey]:
                    tRes += dp(nextKey, stepsLeft - 1)
                return tRes
                
        if N == 0: return 0
        else:
            res = 0
            for i in range(10):
                res += dp(i, N-1)
        return res % mod