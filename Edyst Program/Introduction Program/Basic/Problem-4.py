# Right Arrow Pattern
"""
Write a program to print the Right Arrow Pattern.

Input Format:
Take an input Integer which is from stdin.

Output Format:
print Right Arrow pattern

Example Input:
5

Output:

*****    
  ****   
    ***  
      ** 
        *
      ** 
    ***  
  ****   
***** 


"""

n = int(input())
m = n
step = 0
while m:
    for i in range(step):
        print(" ", end="")
    for i in range(m):
        print("*", end="")
    m -= 1
    step += 2
    print()
step -= 4
for i in range(2, n + 1):
    for j in range(step):
        print(" ", end="")
    for h in range(i):
        print("*", end="")
    print()
    step -= 2
