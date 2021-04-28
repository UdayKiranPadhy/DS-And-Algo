"""
Estimated End Date: 18/02/21
Print middle column
Complete the given method solve which takes as parameter a list of lists called myList. You have to print the middle column of this list.

Example Input:

1 2 3 4 5
6 7 8 9 10
11 12 13 14 25
Output:
3 8 13

Example Input:

2 4 7 1 12
2 3 45 6 13

Output:
7 45
"""


def solve(l):
    mid = int(len(l[0]) / 2)
    for i in l:
        print(i[mid], end=" ")
