"""

Minimum time required to rot all oranges
Difficulty Level : Hard

Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:  

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
Determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.

Examples: 

Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};

Output:
All oranges can become rotten in 2-time frames.
Explanation: 
At 0th time frame:
 {2, 1, 0, 2, 1}
 {1, 0, 1, 2, 1}
 {1, 0, 0, 2, 1}

At 1st time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {1, 0, 0, 2, 2}

At 2nd time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {2, 0, 0, 2, 2}


Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {0, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges cannot be rotten.
Explanation: 
At 0th time frame:
{2, 1, 0, 2, 1}
{0, 0, 1, 2, 1}
{1, 0, 0, 2, 1}

At 1st time frame:
{2, 2, 0, 2, 2}
{0, 0, 2, 2, 2}
{1, 0, 0, 2, 2}

At 2nd time frame:
{2, 2, 0, 2, 2}
{0, 0, 2, 2, 2}
{1, 0, 0, 2, 2}
...
The 1 at the bottom left corner of the matrix is never rotten.

"""
def issafe(i, j):
 
    if (i >= 0 and i < R and
        j >= 0 and j < C):
        return True
    return False
 
def rotOranges(v):
 
    changed = False
    no = 2
    while (True):
        for i in range(R):
            for j in range(C):
 
                # Rot all other oranges
                # present at (i+1, j), 
                # (i, j-1), (i, j+1), 
                # (i-1, j)
                if (v[i][j] == no):
                    if (issafe(i + 1, j) and
                        v[i + 1][j] == 1):
                        v[i + 1][j] = v[i][j] + 1
                        changed = True
 
                    if (issafe(i, j + 1) and
                        v[i][j + 1] == 1):
                        v[i][j + 1] = v[i][j] + 1
                        changed = True
 
                    if (issafe(i - 1, j) and
                        v[i - 1][j] == 1):
                        v[i - 1][j] = v[i][j] + 1
                        changed = True
 
                    if (issafe(i, j - 1) and
                        v[i][j - 1] == 1):
                        v[i][j - 1] = v[i][j] + 1
                        changed = True
 
        # if no rotten orange found 
        # it means all oranges rottened
        # now
        if (not changed):
           break
        changed = False
        no += 1
 
    for i in range(R):
        for j in range(C):
 
            # if any orange is found
            # to be not rotten then 
            # ans is not possible
            if (v[i][j] == 1):
                return -1
 
    # Because initial value
    # for a rotten orange was 2
    return no - 2
 
# Driver function
if __name__ == "__main__":
 
    v = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    R=len(v)
    C=len(v[0])
 
    # print("Max time incurred: ",
    #        rotOranges(v))

"""
Complexity Analysis: 
Time Complexity : O(max(R,C) * R *C). 
The matrix needs to be traversed again and again until there is no change in the matrix, that can happen max(R,C) times. So time complexity is O(max(R,C) * R *C).
Space Complexity:O(1). 
No extra space is required.
"""


# Optimal Approach
# https://youtu.be/03tmEMRDZBk
"""
The idea here is to find the shortest distance of non rotton orange to the rotten orange
and apply the max of the distance and return it.
if the  distance is infinite return -1 .
"""
# Algorithm
# For this we use BFS Approach of graphs to find the minimum distance.
class QueueElement:
    def __init__(self,i,j,T):
        self.i=i
        self.j=j
        self.T=T

def RottonOranges(v):
    list1=[]
    # First append rotton oranges  indexes into list
    for i in range(len(v)):
        for j in range(len(v[0])):
            if v[i][j]==2:
                list1.append(QueueElement(i,j,0))
    print(list1)

v = [[2, 1, 0, 2, 1],
     [1, 0, 1, 2, 1],
     [1, 0, 0, 2, 1]]
RottonOranges(v)