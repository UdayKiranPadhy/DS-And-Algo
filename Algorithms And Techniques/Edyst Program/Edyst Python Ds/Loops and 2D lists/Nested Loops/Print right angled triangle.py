"""
Estimated End Date: 18/02/21
Print the right angle triangle
Given a number n, Complete the given method solve to print right angled number triangle, as given below.

Hera each line contains n-i+1 numbers, where n is the number of rows and i is the row number. The first number of first line is 1.

Print in an increasing order. Reset the order once you reach 9 and then start from 1 again.

The function takes as parameter only 1 integer, n.

Example Input: 3
Example Output:

123
45
6
Example Input: 5
Example Output:

12345
6789
123
45
6
"""


def solve(n):
    count = 1
    for i in range(n):
        for j in range(n - i):
            print(count, end="")
            count += 1
            if count == 10:
                count = 1
        print()


solve(5)