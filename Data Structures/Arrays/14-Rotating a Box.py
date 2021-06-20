"""

https://leetcode.com/contest/biweekly-contest-52/problems/rotating-the-box/

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.


Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]


Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]


Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

"""


def rotateThebox(box: list) -> list[list[str]]:
    for row in box:
        move_position = len(row) - 1
        for j in range(len(row) - 1, -1, -1):
            if row[j] == "*":
                move_position = j - 1
            elif row[j] == "#":
                row[move_position], row[j] = row[j], row[move_position]
                move_position -= 1

    return zip(*box[::-1])


box = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."],
]
print(list(rotateThebox(box)))
