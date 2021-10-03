"""

566. Reshape the Matrix
Easy

In MATLAB, there is a handy function called reshape which can reshape an m x n 
matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing 
the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original 
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

"""

# Problem statement
# https://leetcode.com/problems/reshape-the-matrix/

# Solution
# First approach is to reshape to line and then reshape it to new shape. 
# However we can do smarter: just iterate over all elements line by line 
# and use res[count//c][count%c] = nums[i][j] to fill element by element.

# Complexity
# Time complexity is O(mn), space complexity is O(mn), but in fact it is 
# O(1) if we do not count output array.

# Code
from itertools import product
class Solution:
    def matrixReshape(self, nums, r, c):
        m, n, count = len(nums), len(nums[0]), 0
        if m*n != r*c: return nums
        res = [[0] * c for _ in range(r)]
        for i, j in product(range(m), range(n)):
            res[count//c][count%c] = nums[i][j]
            count += 1      
        return res

# My Post
# https://leetcode.com/problems/reshape-the-matrix/discuss/1495295/Python-or-Explained-or-Easy-to-Understand
