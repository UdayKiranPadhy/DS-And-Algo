"""

Find First and Last Position of Element in Sorted Array
Medium

6974

230

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

# Problem statement
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution
# Use binary search with adaptation twice: once to find the left place and once to find
# the right place. I understand that goal is to write binary search from scratch if you
# are on the interview, but here is solution, using already existing bisect library in
# python. The idea is to use bisect (which is also bisect_right) and bisect_left to get
# the range of numbers: first one will return index before all repetitions of target and
# the second one: after. So, if these two indexes are equal, it means that we did not
# found this element, so we return [-1, -1]. If we found, we return [l, r - 1].

# Complexity
# Time complexity is O(log n), space is O(1).

from bisect import bisect, bisect_left


class Solution:
    def searchRange(self, nums, target):
        l = bisect_left(nums, target)
        r = bisect(nums, target)
        return [-1, -1] if l == r else [l, r - 1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bisect_left(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def bisect_right(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        idx = bisect_left(nums, target)
        if idx < len(nums) and nums[bisect_left(nums, target)] == target:
            return [bisect_left(nums, target), bisect_right(nums, target) - 1]
        return [-1, -1]
