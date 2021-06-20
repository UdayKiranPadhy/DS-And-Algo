# X Pattern

"""
Write a program to take String if the length of String is odd print X pattern otherwise print INVALID.

Input Format:
Take a String as input from stdin.

Output Format:
print the desired Pattern or INVALID.

Example Input:
edyst

Output:

e   t
 d s 
  y  
 d s 
e   t
"""

s = input()
if len(s) % 2 == 0:
    print("INVALID")
else:
    left = 0
    right = len(s) - 1
    space = len(s) - 2
    step = 0
    while space:
        for i in range(step):
            print(" ", end="")
        print(s[left], end="")
        left += 1
        for i in range(space):
            print(" ", end="")
        print(s[right])
        right -= 1
        step += 1
        space -= 2
        if space < 0:
            space = 0
    for i in range(step):
        print(" ", end="")
    print(s[int(len(s) / 2)])
    space = 1
    step -= 1
    left -= 1
    right += 1
    while space != len(s):
        for i in range(step):
            print(" ", end="")
        print(s[left], end="")
        left -= 1
        for i in range(space):
            print(" ", end="")
        print(s[right])
        right += 1
        space += 2
        step -= 1