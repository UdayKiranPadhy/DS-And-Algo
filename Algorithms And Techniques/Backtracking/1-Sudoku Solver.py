"""


https://leetcode.com/problems/sudoku-solver/description/
"""

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize the sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill the sets with pre initilized values
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    number = int(board[i][j])
                    rows[i].add(number)
                    cols[i].add(number)
                    box_id = i//3 + 3*j//3
                    boxes[box_id].add(number)

        def backTrack(i, j):
            nonlocal solved
            if i == 9 and j == 9:
                solved = True
                return
            new_i = i + (j+1)//9
            new_j = (j+1) % 9
            if board[i][j] != '.':
                backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_id = i // 3 * 3 + j//3
                    if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                        rows[i].add(num)
                        cols[i].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)

                        backTrack(new_i, new_j)

                        if not solved:
                            rows.remove(num)
                            cols.remove(num)
                            boxes[box_id].remove(num)
                            board[i][j] = '.'

        solved = False
        backTrack(0, 0)
