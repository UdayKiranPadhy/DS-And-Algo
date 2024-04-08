"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

84. Largest Rectangle in Histogram
Hard
Topics
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        left_smaller = []
        stack = []
        for i in range(N):
            if not stack:
                left_smaller.append(-1)
            elif heights[stack[-1]] < heights[i]:
                left_smaller.append(stack[-1])


model = Solution()
model.largestRectangleArea([2,1,5,6,2,3])