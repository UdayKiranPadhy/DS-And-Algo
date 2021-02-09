"""
Write a program to partition a given array around an element (called the pivot). Given the array and the index of pivot element (passed as parameters to the function), rearrange the numbers in the array so that all elements lesser than the pivot come to the left of it, while all numbers greater than the pivot come to the right of it in the newly rearranged array.

Example Input:

9 -6 6 10 1 -3 -8 -3 -8 -2
9
Output:

-6 -3 -8 -3 -8 -2 6 10 1 9
Note :

Please partition the given array only (instead of returning a new one). You need not print or return anything.
In above example, the index of the pivot element is 9, thus the pivot element is the value -2.
After rearraning the array, all elements (other than the pivot) would be in same order as in the original array.
"""


class Solution:
    def partition(self, A, pivot):
        # write your method here
        low = 0
        high = len(A) - 1
        t = A[pivot]
        i = low - 1
        for j in range(low, high):
            if A[j] <= t:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[high] = A[high], A[i + 1]
        return i + 1
