"""
Link:-https://leetcode.com/problems/house-robber-ii/
Date:-11/6/21

213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has 
a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses 
have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because 
they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000


"""

from functools import lru_cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)

        @lru_cache(None)
        def rob(index, rob1):
            if index >= N:
                return 0
            if index == 0:
                op1 = nums[index] + rob(index + 2, 1)
                op2 = rob(index+1, 0)
                return max(op1, op2)
            elif index == N-1 and rob1 == 1:
                return rob(index+1, 1)
            else:
                op1 = nums[index]+rob(index + 2, rob1)
                op2 = rob(index+1, rob1)
                return max(op1, op2)
        return rob(0, 0)
