# Left Arrow Pattern

"""
Write a program to print the Left Arrow Pattern.You need to do that by  using two for loops only.

Input Format:
Take integer input from stdin.

Output Format:
Print the desired Pattern.

Example Input:
5

Output:

* * * * * * * * * * 
* * * * * * * * 
* * * * * * 
* * * * 
* * 
* * 
* * * * 
* * * * * * 
* * * * * * * * 
* * * * * * * * * *

"""

n = int(input())

l = input().split(" ")
l2 = []
for i in l:
    l2.append(int(i))
print(max(l2))