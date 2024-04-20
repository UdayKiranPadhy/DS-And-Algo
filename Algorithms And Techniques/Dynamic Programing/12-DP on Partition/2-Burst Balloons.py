"""

URL: https://leetcode.com/problems/burst-balloons/description/

312. Burst Balloons

GoogleMicrosoftAppleBloombergUberYou are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 
Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:

Input: nums = [1,5]
Output: 10

 
Constraints:

	n == nums.length
	1 <= n <= 300
	0 <= nums[i] <= 100

"""

# https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=52&ab_channel=takeUforward

# Go from bottom not from top

from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums.insert(0, 1)
        nums.append(1)

        @cache
        def go(i, j):
            if i > j: return 0
            maxi = -float('inf')
            for index in range(i, j + 1):
                maxi = max(maxi, nums[i - 1] * nums[index] * nums[j + 1] + go(i, index - 1) + go(index + 1, j))
            return maxi

        return go(1, N)
