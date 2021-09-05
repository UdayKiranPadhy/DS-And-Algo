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
        
        def backTrack(i,j):
            nonlocal solved
            if i == 9 and j == 9:
                solved = True
                return
            new_i = 


        solved = False
        backTrack(0,0) 