"""

413. Arithmetic Slices
Medium


https://leetcode.com/problems/arithmetic-slices/

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000


"""

# Solution 1: Bottom up DP

# Let dp[i] denote the number of arithmetic subarray ends at nums[i].
# If if nums[i-1] - nums[i-2] == nums[i] - nums[i-1] then we can form the Arithmetic subarray
# ends at nums[i].
# So dp[i] = dp[i-1] + 1.
# For example: nums = [1, 3, 5, 7, 9]
# dp[2] = 1 arithmetic subarrays are {1, 3, 5}
# dp[3] = dp[2] + 1 = 2, arithmetic subarrays are {1, 3, 5, 7}, {3, 5, 7}
# dp[4] = dp[3] + 1 = 3, arithmetic subarrays are {1, 3, 5, 7, 9}, {3, 5, 7, 9}, {5, 7, 9}
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans


# Complexity
# Time: O(N), where N <= 5000 is length of nums array.
# Space: O(N)


# ✔️ Solution 2: Bottom up DP (Space Optimized)

# Since our dp only access current dp state dp and previous dp state dpPrev.
# So we can easy to achieve O(1) in space.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp, dpPrev = 0, 0
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dpPrev + 1
            ans += dp
            dpPrev = dp
            dp = 0
        return ans
# Complexity

# Time: O(N), where N <= 5000 is length of nums array.
# Space: O(1)
