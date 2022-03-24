

"""

221. Maximal Square
Medium

Given an m x n binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.


"""


# Problem statement
# https://leetcode.com/problems/maximal-square/

# Solution
# Classical DP problem, where by dp[i][j] we define the biggest square whose bottom
# right corner is the cell with index (i,j) in the original matrix. Then we can
# use dp(i, j)= min(dp(i-1, j), dp(i-1, j-1), dp(i, j-1)) + 1 to update cells,
# if we have 1 in (i, j) place in original matrix.

# Complexity
# Time complexity is O(mn) and the same space. Space complexity can be reduced
# to O(min(m, n)), because we use only one row at a time.


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {}

        def helper(r, c):
            if r >= len(matrix) or c >= len(matrix[0]):
                return 0

            if (r, c) not in cache:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2
