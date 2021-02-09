"""
Write a program to take an 1D integer array which is sorted  and also another integer, the key. You have to find whether the key exists in the list or not. If the key does not exist, print -1. Otherwise, print 1.

Input Format:

First line take an Integer input from stdin which is array length n.
Second line take n Integers which is inputs of array.
Third line take an Integer input which is key to search.
Output Format:

Print 1 when key is present otherwise print -1.

Example Input:
5
1  2 4 5 6
2

Output:
1

Example Input:
6
5 6 7 8 9 10
3

Output:
-1
"""
_ = int(input())
l = list(map(int, input().split(" ")))
key = int(input())

if key in l:
    print("1")
else:
    print("-1")