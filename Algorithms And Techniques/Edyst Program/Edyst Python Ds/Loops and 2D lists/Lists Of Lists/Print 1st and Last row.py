"""
Print first and last row
Complete the given method solve which takes as parameter a list of lists called myList. You have to print the first and last row of this list.

Example Input:
1 2 3 4 5
6 7 8 9 10
11 12 13 14 25
Output:
1 2 3 4 5
11 12 13 14 25

Example Input:
2 4 7 1
2 3 45 6
7 89 15 16
Output:
2 4 7 1
7 89 15 16
"""

def solve(myList):
    for i in myList[0]:
        print(i,end=" ")
    print("\n",end="")
    for i in myList[-1]:
        print(i,end=" ")