"""

Search Insert Position
Easy

4401

314

Add to List

Share
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""


# https://leetcode.com/problems/search-insert-position

# Solution 1: bisect
# It is not said in the problem statement not to use any libraries, so why
# not use bisect_left function, so conviniently provided by python? Why we
# use bisect_left? Because for [1,3,5,6] and number 5 we need to return
# index 2: if element is already present in array, the insertion point will
# be before (to the left of) any existing entries.

# Complexity is classical for binary search: O(log n)

import bisect


class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)


# Solution 2: Classical binary search
# Classical binary search problem, where we need to return beg in the end,
# because we are looking for left place to insert our symbol.

class Solution:
    def searchInsert(self, nums, target):
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg
