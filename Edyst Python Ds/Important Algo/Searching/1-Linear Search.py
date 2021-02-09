"""
Find Element Using Linear Search

Write a program to take an 1D integer array and also another integer, the key. You have to find the position of the key in the array. If the key does not exist, print No. Otherwise, print the index.

Input Format:

First line take an Integer input from stdin which is array length n.
Second line take n Integers which is inputs of array.
Third line take an Integer input which is key to search.
Output Format:

Print Index when key is present otherwise print No.

Note: If the key exists in more than one index, choose that index which has higher value.

Example Input:
5
1 3 2 4 5
2

Output:
2

Example Input:
4
4 2 7 3
9

Output:
No
"""

_ = input()
A = list(map(int, input().split(" ")))
key = int(input())
found = False
position = -1

for i in range(len(A)):
    if A[i] == key:
        found = True
        position = i

if found:
    print(position)
else:
    print("No")
