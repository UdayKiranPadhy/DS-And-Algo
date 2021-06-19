"""

Source :- HackWithInfy Sample Question
Date 15/06/2021

Minimum Pluses
Given an equation x=y, for example, 111=12, you need to add pluses inside x to make the 
equation correct. In our example, 111=12 , we can add one + to make the equation correct: 1+11=12.

You need to find the minimum number of pluses to add to x to make the equation correct. 
If there is no answer, print -1

Note the the value of y won't exceed 5000. The numbers in the correct equation may contain 
arbitrary amounts of leading zeros.

Input Format
The first line contains a string A as described in the problem statement.

Constraints
1<=len(A)<=103

Example Input #1
111=12
Output
1

Example Input #2
12374923=121
Output
3
Explanation
12+37+49+23=121

"""

import sys
from functools import lru_cache


@lru_cache(None)
def minimum_pluses(string, total, sum_until_now):
    """
    12154= 1219
    23=5
    """
    if sum_until_now + int(string) == total:
        return 0
    if string == "":
        return sys.maxsize

    pluses = sys.maxsize
    for i in range(1, len(string)):
        pluses = min(
            pluses, 1 + minimum_pluses(string[i:], total, sum_until_now + int(string[:i])))
    return pluses


string = input().strip().split("=")
given = string[0]
total = int(string[1])

print(minimum_pluses(given, total, 0))
