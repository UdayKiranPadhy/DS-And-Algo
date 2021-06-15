"""

Goldmine
Given a gold mine of m x n dimensions.

Each field in this mine contains a positive integer which is the amount of gold present at that position.
Initially the miner is at first column but can be at any row.
He can move only int three directions: right, right-up and right-down. That is, east, northeast and southeast from a given cell
Starting from any row (but always the first column), find out the maximum amount of gold that the miner can collect.

Input format

The first line contains T, the number of test cases. The following T lines contain 2 integers m and n which tell us the rows and columns respectively. This is followed by all the 2D array elements in a single line, separated by space

Output format

For each test case, output the maximum number of gold collected
Example Input #1

1
4 4 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
Output #1

16
Explanation:

(2,0) -> (1,1) -> (1,2) -> (0,3)  OR  (2,0) -> (3,1) -> (2,2) -> (2,3)


"""
import sys
from functools import lru_cache


@lru_cache(None)
def max_path(i, j, t):
    if i < 0 or j < 0 or i > m-1 or j > n-1:
        return -sys.maxsize
    elif j == n-1 and i >= 0 and i <= m-1:
        return land[i][j]
    else:
        return land[i][j] + max(max_path(i-1, j+1, t), max_path(i, j+1, t), max_path(i+1, j+1, t))


for t in range(int(input())):
    string = [int(x) for x in input().strip().split(" ")]
    m = string[0]
    n = string[1]
    land = []
    start = 2
    for i in range(m):
        land.append(string[start:start+n])
        start += n
    del string, start
    maxi = -sys.maxsize - 1
    for i in range(m):
        cost = max_path(i, 0, t)
        maxi = max(maxi, cost)
    print(maxi)
