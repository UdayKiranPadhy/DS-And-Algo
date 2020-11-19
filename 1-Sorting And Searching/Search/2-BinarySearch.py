# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
# A simple approach is to do linear search.
# The time complexity of above algorithm is O(n). 
# Another approach to perform the same task is using Binary Search.

# Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
# Begin with an interval covering the whole array. 
# If the value of the search key is less than the item in the middle of the interval, 
# narrow the interval to the lower half. Otherwise narrow it to the upper half. 
# Repeatedly check until the value is found or the interval is empty.

def search(arr,left,right, n):

    if right >= left:
        mid = left + (right -1) // 2

        if arr[mid] == n :
            return mid

        if n > arr[mid]:
            return search(arr , mid , right , n)
        
        if n < arr[mid]:
            return search(arr , low , mid ,n)
    
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
        