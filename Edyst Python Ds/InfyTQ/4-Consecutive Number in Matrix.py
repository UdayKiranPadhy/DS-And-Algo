"""

You are given an m*n matrix such that n = m+1. In the given matrix, find if any number is consecutive for 3 times either in row, column, diagonals print the num.

If there are multiple such numbers then print minimum of those numbers.

Input format
First line contains m, the number of rows
Following m lines contain n numbers
Example Input

6
2 3 4 5 6 2 4
2 3 4 7 6 7 6
2 3 5 5 5 5 2
2 3 1 1 2 1 3
1 1 1 1 9 0 3
2 3 1 1 5 1 2
Output

1

"""

m=int(input())
n=m+1
numbers = []
matrix=[[0 for j in range(n)] for i in range(m)]
print(matrix)