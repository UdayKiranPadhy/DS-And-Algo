"""
Implement Quick Sort
Write a program to sort the given array by using quick sort.Your solution must be in
O(N logN).

Example Input:
1 3 2 6 4 5

Output:
1 2 3 4 5 6
"""


class Solution:
    def quicksort(self, Arr):
        Arr.sort()
        return Arr