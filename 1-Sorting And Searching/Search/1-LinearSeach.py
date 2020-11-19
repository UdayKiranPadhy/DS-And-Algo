# Linear Search

# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

# Examples :  

# Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6

# Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                      110, 100, 130, 170}
#            x = 175;
# Output : -1
# Element x is not present in arr[].

# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of elements, return -1.

def search(arr , n):
    count=1
    for i in arr:
        if n == i:
            return count
        count +=1
    return -1

# The time complexity of the above algorithm is O(n). 

# Type2 of linear Search:- Apply linear Search from the both sides of the list

def search2(arr , n):
    left = 0
    right = len(arr) - 1
    for i in range(0,len(arr)):
        if left > right:
            return -1
        if arr[left] == n:
            return left + 1
        left +=1

        if arr[right] == n:
            return right + 1
        right -=1




# Doubts :-
#     for (left = 0; left <= right;) 
# How to get that condition in python