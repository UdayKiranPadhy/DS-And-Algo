"""
Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

# Problem statement
# https://leetcode.com/problems/valid-sudoku/

# Solution
# We just need to check all 27 conditions - for every row, every column and every square.

# First 3 lines of code to check rows and columns: we check each row in board and in 
# transposed board *board and collect all elements which are not equal to .
# Next 4 lines of code to check all 9 cells: first we create all centers of 3x3 cells 
# and then again collect all elements, not equal to .
# Complexity
# Time complexity is O(n^2), where n is size of board, space complexity is O(n).

# Code
from itertools import chain , product
class Solution:
    def isValidSudoku(self, board):
        for row in chain(board, zip(*board)):
            cand = [i for i in row if i != "."]
            if len(set(cand)) != len(cand): return False
            
        for x, y in product([1,4,7],[1,4,7]):
            cand = [board[x+i][y+j] for i,j in product([-1,0,1],[-1,0,1])]
            cand = [i for i in cand if i != "."]
            if len(set(cand)) != len(cand): return False
        
        return True



board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

model = Solution()
model.isValidSudoku(board)