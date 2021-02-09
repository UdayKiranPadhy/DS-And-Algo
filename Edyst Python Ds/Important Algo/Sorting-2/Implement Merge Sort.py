"""
Write a program to sort the given array by using merge sort.Your solution must be in
O(N logN).

Example Input:
1 3 2 1 4 5

Output:
1 1 2 3 4 5
"""

class Solution:
    def mergesort(self, l):
        if len(l)>1:
            mid=len(l)//2
            left = l[:mid]
            right=l[mid:]
            
            Solution.mergesort(self,left)
            Solution.mergesort(self,right)
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    l[k] = left[i]
                    i += 1
                    k += 1
                else:
                    l[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                l[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                l[k] = right[j]
                j += 1
                k += 1
            return l