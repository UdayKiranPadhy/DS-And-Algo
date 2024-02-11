"""

45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000


"""
# My Trails TLE
from functools import lru_cache


class Solution:
    def jump(self, nums: list[int]) -> int:

        @lru_cache(None)
        def jumps(index, jumpss):
            if index == len(nums)-1:
                return jumpss
            best = 999999999
            for i in range(1, nums[index]+1):
                if index + i <= len(nums)-1:
                    best = min(best, jumps(index + i, jumpss + 1))
            return best
        return jumps(0, 0)


# Accepted My Trails
class Solution:
    def jump(self, nums: list[int]) -> int:

        @lru_cache(None)
        def jumps(index):
            if index == len(nums)-1:
                return 0
            best = 99999
            for i in range(1, nums[index]+1):
                if index + i < len(nums):
                    best = min(best, jumps(index+i))
            return best + 1
        return jumps(0)

# Time Complexity is O(N^2)

# Better Solution is Greedy Solution O(n)


class Solution:
    def jump(self, nums):
        farthest = 0
        current = 0
        jumps = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current:
                current = farthest
                jumps += 1
        return jumps



# Same Question https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1 from GFG
sl