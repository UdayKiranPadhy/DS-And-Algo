"""

119. Pascal's Triangle II
Easy

https://leetcode.com/problems/pascals-triangle-ii/


Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Base case
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        res = []

        # First eleemnt is always 1
        res.append(1)

        # Iterate previous layers to get the middle values
        for p in range(len(prev) - 1):
            val = prev[p] + prev[p + 1]
            res.append(val)

        # Last element is always 1
        res.append(1)
        return res
