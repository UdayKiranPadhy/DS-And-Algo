"""
Upper Diagonal Triangle
Complete the given method solve that takes as parameter an integer n and creates an nxn triangular pattern like the examples below.

Example Input: 3

Example Output:
***
.**
..*

Example Input: 5

Example Output:
*****
.****
..***
...**
....*
"""


def solve(n):
    for i in range(1, n + 1):
        for _ in range(i - 1):
            print(".", end="")
        for _ in range(n + 1 - i):
            print("*", end="")
        print()