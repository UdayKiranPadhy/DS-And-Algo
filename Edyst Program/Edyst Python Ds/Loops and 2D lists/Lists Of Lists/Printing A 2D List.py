"""

Printing a 2D List
Complete the given method solve which takes as parameter a list of lists called myList

You must print the contents of myList

Example Input:
1 9 3
2 4 6
10 75 2

Output:
1 9 3
2 4 6
10 75 2
"""
def solve(mylist):
    for i in mylist:
        for j in i:
            print(j,end=" ")
        print()