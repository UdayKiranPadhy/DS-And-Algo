"""

42. Trapping ter
Hard

Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of ter (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""


# Method 1 Dynamic Programming
# See Solution 1 Image for Better understanding

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        max_left = -1
        leftmax = [0] * N
        for i in range(N-1, -1, -1):
            if height[i] > max_left:
                max_left = height[i]
            leftmax[i] = max_left

        max_right = -1
        rightmax = [0] * N
        for i in range(N):
            if height[i] > max_right:
                max_right = height[i]
            rightmax[i] = max_right

        water = [0] * N
        for i in range(N):
            water[i] = min(leftmax[i], rightmax[i]) - height[i]

        return sum(water)
