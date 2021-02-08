"""
InfyTQ - Pairs with equal sums
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array.

Note:

Return the indices A1 B1 C1 D1, so that
A[A1] + A[B1] = A[C1] + A[D1]
A1 < B1, C1 < D1
A1 < C1, B1 != D1, B1 != C1

If there are more than one solutions, then return the tuple of values which are lexicographical smallest.
Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff

A1 < A2 OR
A1 = A2 AND B1 < B2 OR
A1 = A2 AND B1 = B2 AND C1 < C2 OR
A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Input :

A = [3, 4, 7, 1, 2, 9, 8]

Output :
[0, 2, 3, 5] (O index)

Note : If no solution is possible, return an empty list.
"""

class Solution:
    def equal(self, A):
        index=[]
        if len(A)>3:
            for i in range(len(A)-3):
                for j in range(i+1,len(A)-2):
                    for k in range(j+1,len(A)-1):
                        for l in range(k+1,len(A)):
                            if A[i]+A[j]==A[k]+A[l]:
                                index.append([i,j,k,l])
            return index[0]
        else:
            return []

met=Solution()
print(met.equal([9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -5, -5, -5, -5, -5, -5, -5, -6, -6, -7, -7, -7, -7, -7, -7, -7, -7, -8, -8, -8, -8, -8, -9, -9, -9, -9, -9]))