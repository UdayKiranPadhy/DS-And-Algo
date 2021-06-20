"""
Find Addition of Matrices
In maths, the sum of 2 matrices A and B will be a matrix which has the same number of rows and columns as do A and B. The sum of A and B, denoted A + B, is computed by adding corresponding elements of A and B.

Example:

1 2   +   5 5
3 4       5 5
is:

6 7
8 9
Given 2 matrices of same dimensions, you have to print the sum of the 2 matrices.

Complete the given method solve which takes as parameter A and B and prints the sum of the 2 matrices.

Example Input:
A:
1 1
1 1
B:
9 8
0 0
Output:
10 9
1 1
"""

def solve(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j]+B[i][j],end=" ")
        print()