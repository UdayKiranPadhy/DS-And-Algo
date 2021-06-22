"""
A number is a COLORFUL number, if the product of every digit of a contiguous subsequence is different.

A number can be broken into different contiguous sub-subsequence parts.

Suppose, a number = 3245, it can be broken into parts like 3 2 4 5 32 24 45 324 245 and since the product of every digit of a contiguous subsequence is different therefore 3245 is COLORFUL number.

Given a number A, return 1 if A is COLORFUL else return 0.

Input :
3245

Output :
1
"""

class Solution:
    def colorful(self, A):
        A = str(A)
        A = list(A)
        A = list(map(int, A))
        p = set()
        for i in range(len(A)):
            prod = 1
            for j in range(i, len(A)):
                prod *= A[j]
                if prod in p:
                    return 0
                p.add(prod)
        return 1