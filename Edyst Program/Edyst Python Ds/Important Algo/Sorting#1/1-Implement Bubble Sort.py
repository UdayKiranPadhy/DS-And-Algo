"""
Write a program to sort the given array by using Bubble sort

Example Input:
1 3 2 6 4 5

Output:
1 2 3 4 5 6
"""

class Solution:
    def bubbleSort(self, Arr):
        # write your method here
        n=len(Arr)
        for i in range(len(Arr)): 
  
        # Last i elements are already in place 
            for j in range(0, n-i-1): 
                if Arr[j] > Arr[j+1] : 
                    Arr[j], Arr[j+1] = Arr[j+1], Arr[j] 
        #print(Arr)
        return Arr

class Solution:
    def bubbleSort(self, arr):
        n=len(arr)
        # Traverse through all array elements 
        for i in range(n): 
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr