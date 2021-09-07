"""

286	Walls and Gates

 You are given a m x n 2D grid initialized with these three possible values.

 -1     - A wall or an obstacle.
 0      - A gate.
 INF    - Infinity means an empty room.
            We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that
            the distance to a gate is less than 2147483647.

 Fill each empty room with the distance to its nearest gate.
 If it is impossible to reach a gate, it should be filled with INF.

 For example, given the 2D grid:

 INF    -1      0       INF
 INF    INF     INF     -1
 INF    -1      INF     -1
 0      -1      INF     INF

 After running your function, the 2D grid should be:

 3  -1   0   1
 2   2   1  -1
 1  -1   2  -1
 0  -1   3   4

 @similar: 317	Shortest Distance from All Buildings

"""


# Algorithm
# Search for the position of 0, and every time a 0 is found, start DFS traversal with four
# adjacent points around it as the starting point, and bring in the depth value 1.

# If the value encountered is greater than the current depth value, assign the position
# value to the current depth value, and start DFS traversal for the four adjacent points
# of the current point. Note that the depth value needs to be increased by 1.

# After the traversal is completed, all positions are updated correctly

from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        d = deque()

        def addRooms(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            visited.add((r, c))
            d.append([r, c])

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    d.append([i, j])

        dist = 0
        while len(d) != 0:
            for _ in range(len(d)):
                r, c = d.popleft()
                rooms[r][c] = dist
                addRooms(r+1, c)
                addRooms(r-1, c)
                addRooms(r, c+1)
                addRooms(r, c-1)
            dist += 1
