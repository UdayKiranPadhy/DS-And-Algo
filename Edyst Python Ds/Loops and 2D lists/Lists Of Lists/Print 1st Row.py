"""
Print First Row
Complete the given method solve which takes as parameter a list of lists called myList. You have to print the first row of this list.

Example Input:
1 2 3 4 5
6 7 8 9 10
Output:
1 2 3 4 5

Example Input:
2 4 7 1
2 3 45 6
7 89 15 16
Output:
2 4 7 1
"""
def solve(A):
    for i in A:
        for j in i:
            print(j,end=" ")
        break