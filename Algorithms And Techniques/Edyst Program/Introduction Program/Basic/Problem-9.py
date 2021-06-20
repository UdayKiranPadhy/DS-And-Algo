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
m = n
s = 0
while n:
    for i in range(2 * n):
        print("* ", end="")
    print()
    n -= 1
    if n < 0:
        s = n
        n = 0
s += 2
for i in range(0, m, 1):
    for i in range(s):
        print("* ", end="")
    print()
    s += 2