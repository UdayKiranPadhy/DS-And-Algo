"""

A heightful number triangle
Complete the given method solve that takes as parameter an integer n and prints the pattern like in the examples. Note that n represents the number of rows.

Note: n will be less than or equal to 13

Example Input: 5

Output:
15
14.10
13.09.06
12.08.05.03
11.07.04.02.01

Example Input: 7

Output:
28
27.21
26.20.15
25.19.14.10
24.18.13.09.06
23.17.12.08.05.03
22.16.11.07.04.02.01

"""


def solve(n):
    num = int(n * (n + 1) / 2)
    for i in range(1, n + 1):
        if i == 1:
            print(num, end=" ")
        else:
            print(num, end=".")
        sub = n - 1
        for j in range(i - 1):
            if j == 0:
                temp = num - sub
            else:
                temp = temp - sub
            if j == i - 2:
                print(gg(num, temp), end="")
            else:
                print(gg(num, temp), end=".")
            sub -= 1
        print()
        num -= 1


def gg(num1, num2):
    l=[]
    if len(str(num1)) == len(str(num2)):
        return num2
    else:
        pad=len(str(num1)) - len(str(num2))
        for i in range(pad):
            l.append(str(0))
        l.append(str(num2))
        stri = "".join(l)
        return stri

solve(5)