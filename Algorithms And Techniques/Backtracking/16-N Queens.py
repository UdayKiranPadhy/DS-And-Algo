"""

https://leetcode.com/problems/n-queens/

51. N-Queens
Hard

12069

275

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9

"""


class Solution:
    def solveNQueens(self, n: int) -> list:
        answer = []

        def backtrack(board, i, column_bit_mask, diagonal_bit_mask1, diagonal_bit_mask2):
            if i == n:
                answer.append(["." * j + "Q" + "." * (n - j - 1) for j in board])
            for j in range(n):
                if column_bit_mask & 1 << j or diagonal_bit_mask1 & 1 << i - j + n or diagonal_bit_mask2 & 1 << i + j:
                    continue
                backtrack(board + [j], i + 1, column_bit_mask ^ 1 << j, diagonal_bit_mask1 ^ 1 << i - j + n,
                          diagonal_bit_mask2 & 1 << i + j)

        backtrack([], 0, 0, 0, 0)
        return answer


class Solution:
    def solveNQueens(self, n):
        def dfs(board, i, c1, c2, c3):
            if i == n: ans.append(["." * j + "Q" + "." * (n - j - 1) for j in board])

            for j in range(n):
                if c1 & 1 << j or c2 & 1 << i - j + n or c3 & 1 << i + j: continue
                dfs(board + [j], i + 1, c1 ^ 1 << j, c2 ^ 1 << i - j + n, c3 ^ 1 << i + j)

        ans = []
        dfs([], 0, 0, 0, 0)
        return ans