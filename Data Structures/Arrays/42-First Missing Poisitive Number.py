"""
https://leetcode.com/problems/first-missing-positive/description/

First Missing Positive
Hard

6939

1107

Add to List

Share
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

"""


# Method 1

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        ans = 0
        flag = 1
        
        while flag == 1:
            if ans+1 in nums:
                ans += 1
            else:
                flag = 0
        
        return ans+1


# Method 2

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+3):
            if i not in nums:
                return i