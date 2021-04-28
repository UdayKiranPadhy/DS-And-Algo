# Printing Diagonal of 2D Array

"""
Write a Program to take 2d Integer Array then you have to print the Right diagonal elements in that Array.

Input Format:

The first line take Integer inputs of row and colomn from stdin.
In Second line take the values of 2d array according to its row and colomn value.
Output Format:

Print the Integers Which is right diagonal elements of 2d Array by space separated.

Example Input:

3 3
1 2 3
4 5 6
7 8 9

Output:
1 5 9

Example Input:

3 4
1 1 1 1
2 2 2 2
3 3 3 3

Output:
1 2 3

"""

m = int(input())
n = int(input())
s = input().split(" ")
list2 = []
start = 0
for i in range(m):
    end = start + n
    list2.append(s[start:end])
    start = end

mini = m if m <= n else n
step = 0
retur = ""
for i in range(mini):
    retur += list2[i][step] + " "
    step += 1
print(retur)