"""

https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description

801. Minimum Swaps To Make Sequences Increasing
Solved
2066
Hard
Topics
Companies
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].



Example 1:

Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation:
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.
Example 2:

Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
Output: 1


Constraints:

2 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 2 * 105

"""
from functools import cache
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.insert(0, -1)
        nums2.insert(0, -1)
        N = len(nums1)

        @cache
        def go(index, swaped):
            if index == N:
                return 0

            prev1 = nums1[index - 1]
            prev2 = nums2[index - 1]

            if swaped:
                prev1, prev2 = prev2, prev1

            ans = float('inf')

            if nums1[index] > prev1 and nums2[index] > prev2:
                ans = go(index + 1, 0)
            if nums1[index] > prev2 and nums2[index] > prev1:
                ans = min(ans, 1 + go(index + 1, 1))

            return ans

        return go(1, 0)

model = Solution()
model.minSwap([3,3,8,9,10],[1,7,4,6,8])