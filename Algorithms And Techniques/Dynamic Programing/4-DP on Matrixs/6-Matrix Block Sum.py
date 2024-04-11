"""
https://leetcode.com/problems/matrix-block-sum/description/

1314. Matrix Block Sum

Medium

Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100

"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1]

        ans = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                row1, col1 = max(0, r - k), max(0, c - k)
                row2, col2 = min(R - 1, r + k), min(C - 1, c + k)
                ans[r][c] = sumRegion(row1, col1, row2, col2)
        return ans