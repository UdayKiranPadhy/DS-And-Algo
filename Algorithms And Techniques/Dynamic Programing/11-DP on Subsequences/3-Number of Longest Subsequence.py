"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

673. Number of Longest Increasing Subsequence
Medium
Topics
Companies
Amazon
Google
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.



Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.


Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106

"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        count = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
        maxi = max(dp)
        ans = 0
        for i in range(N):
            if dp[i] == maxi: ans += count[i]
        return ans
