"""
Print the number pattern
Write a program that reads an input n from stdin. n tells us the number of rows to be printed. Print the pattern as per the given examples.

Input format: Read the value of n

Example Input:
3
Output:

1
1 2
1 2 3
Input:
5
Output:

1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5

"""
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
