"""
Write a program to sort the given array by using Insertion sort

Example Input:
1 3 3 2 1 2

Output:
1 1 2 2 3 3
"""

class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):   
            key = arr[i] 

            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key
        return arr