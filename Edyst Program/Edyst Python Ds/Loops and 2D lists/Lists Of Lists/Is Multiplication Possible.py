"""
Is Multiplication Possible?
> In mathematics, two matrices can only be multiplied if the number of columns in the first matrix is the same as the number of rows in the second matrix.
Given 2 matrices stored in 2 different 2D lists, you have to tell whether multiplication between them is possible.

Complete the given method solve which takes as parameter 2 matrices A and B

Example Input:
1 5 7
2 6 9
-7 -8
-2 -4
-6 -1
Example Output:
Possible

Example Input:
1 5 7
2 6 9
-7 -8
-2 -4
Example Output:
Impossible
"""

def solve(A,B):
    if len(A[0])==len(B):
        print("Possible")
    else:
        print("Impossible")