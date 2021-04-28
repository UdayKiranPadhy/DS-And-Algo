# Maximum Absolute Difference

"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]
 
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
 
So, we return 5.
"""


class Solution:
    def maxArr(self, A):
        l = list(map(int, A))
        n = len(l)
        t = []
        for i in range(n):
            h = []
            for j in range(n):
                h.append(0)
            t.append(h)
        import sys

        maxi = -sys.maxsize - 1
        for i in range(n):
            for j in range(n):
                t[i][j] = f(l, i, j)
                if maxi < f(l, i, j):
                    maxi = f(l, i, j)
        return maxi


def f(l, num1, num2):
    return abs(l[num1] - l[num2]) + abs((num1 + 1) - (num2 + 1))