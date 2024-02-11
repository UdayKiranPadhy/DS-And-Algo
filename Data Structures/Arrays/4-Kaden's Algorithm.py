"""
53. Maximum Subarray

Medium

Given an integer array nums, find the subarray
with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
from typing import List


# Solution 1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        sum = 0

        for i in nums:
            # As soon as you enter 1st add sum
            sum += i

            max_sum = max(max_sum, sum)

            # While you go ensure you are not caring -ve weights
            if sum < 0:
                sum = 0

        return max_sum


#Solution 2

# Solution 1
# We can easily do it with DP in O(n) time. Define by dp[i] maximum sum ending with element with index i.
# Then we have two options: either continue subarray or take single element.

# Complexity
# Time and space is O(n).

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        for i in range(1,N):
            dp[i] = max(nums[i], nums[i]+ dp[i-1])
        return max(dp)