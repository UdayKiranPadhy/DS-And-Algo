"""
Write a program to sort the given array by using Selection sort

Example Input:
1 3 3 2 1 2

Output:
1 1 2 2 3 3
"""

class Solution:
    def selectionSort(self, A): 
        for i in range(len(A)): 
            # Find the minimum element in remaining  
            # unsorted list 
            min_index = i 
            for j in range(i+1, len(A)): 
                if A[min_index] > A[j]: 
                    min_index = j       
            A[i], A[min_index] = A[min_index], A[i] 
        return A