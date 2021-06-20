"""
BowTie Pattern
Complete the given method solve that takes as parameter an integer n and prints a formation like the examples below.

Hint: Is there a relation between row number and the number of *? What about row number and number of .?

Example Input: 1
Example Output:

*.*
***
*.*
Example Input: 5
Example Output:

*.........*
**.......**
***.....***
****...****
*****.*****
***********
*****.*****
****...****
***.....***
**.......**
*.........*

"""


def solve(n):
    cols = 2 * n + 1

    for i in range(1, n + 1):
        for j in range(1, cols + 1):
            if j <= i or j >= cols - i + 1:
                print("*", end="")
            else:
                print(".", end="")
        print()

    # Print 2n +1 stars
    for i in range((2 * n + 1)):
        print("*", end="")
    print()

    # Print Pattern 2

    for i in range(n, 0, -1):
        for j in range(1, cols + 1):
            if j <= i or j >= cols - i + 1:
                print("*", end="")
            else:
                print(".", end="")
        print()