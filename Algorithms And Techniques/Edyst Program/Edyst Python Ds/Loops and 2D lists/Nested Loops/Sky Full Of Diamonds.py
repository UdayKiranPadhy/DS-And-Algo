"""
Sky full of diamonds
Complete the given method solve that takes as parameter an integer n and prints a diamond like the examples below.

Hint: How many rows are there for a number n? How many columns? How many . on each row? How many * on each row?

Example Input: 4
Output:

....*....
...***...
..*****..
.*******.
*********
.*******.
..*****..
...***...
....*....
Example Input: 2
Output:

..*..
.***.
*****
.***.
..*..
Sky full of diamonds
Complete the given method solve that takes as parameter an integer n and prints a diamond like the examples below.

Hint: How many rows are there for a number n? How many columns? How many . on each row? How many * on each row?

Example Input: 4
Output:

....*....
...***...
..*****..
.*******.
*********
.*******.
..*****..
...***...
....*....
Example Input: 2
Output:

..*..
.***.
*****
.***.
..*..

"""


def solve(n):
    star = 1
    dot = n
    for i in range(n):
        for i in range(dot):
            print(".", end="")
        for i in range(star):
            print("*", end="")
        for i in range(dot):
            print(".", end="")
        dot -= 1
        star += 2
        print()

    for i in range(2 * n + 1):
        print("*", end="")
    print()
    dot += 1
    star -= 2
    for i in range(n):
        for i in range(dot):
            print(".", end="")
        for i in range(star):
            print("*", end="")
        for i in range(dot):
            print(".", end="")
        dot += 1
        star -= 2
        print()

solve(2)