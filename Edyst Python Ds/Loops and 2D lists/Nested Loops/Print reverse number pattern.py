"""
Print the reverse of number pattern

Write a program that reads an input n from stdin. n tells us the number of rows to be printed. Print the pattern as per the given examples.

Input format: Read the value for n

Example Input:
3
Output:

3
3 2
3 2 1
Input:
5
Output:

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()
