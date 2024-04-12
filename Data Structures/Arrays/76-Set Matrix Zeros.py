"""
https://leetcode.com/problems/set-matrix-zeroes/description/

73. Set Matrix Zeroes
Solved
Medium
Topics
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


"""
from typing import List


# We take two bit mask row_mask and column_mask traking all the rows and columns we need to mark as zero . The code
# shall be self understanding.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_mask = column_mask = 0
        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row_mask |= (1 << i)
                    column_mask |= (1 << j)

        for i in range(R):
            for j in range(C):
                if row_mask & (1 << i):
                    matrix[i][j] = 0
                if column_mask & (1 << j):
                    matrix[i][j] = 0