"""

Print the repeating pattern
Write a program that reads an input n from stdin. n tells us the number of rows to be printed. Print the pattern as per the given examples.

Input format: Read the value for n

Example Input:
3
Output:

1
2 2
3 3 3
Example Input:
5
Output:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()