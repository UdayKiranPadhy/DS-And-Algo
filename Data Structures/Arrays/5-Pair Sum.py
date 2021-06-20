"""

Given an array A[] and a number x, check for pair in A[] with sum as x
Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. 

Examples: 

Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2
Output: -3, 1
If we calculate the sum of the output,
1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
Output: -1

"""


def PairSum(arr, k):
    # If the arr is not sorted the sorted it first
    arr.sort()
    i = 0
    j = len(arr) - 1

    # Similarly to maximum sub array we have to move the j and i positions
    while i < len(arr) and j > 0 and j > i:
        if arr[i] + arr[j] == k:
            return [i, j]
        elif arr[i] + arr[j] < k:
            i += 1
        else:
            j -= 1
    else:
        return -1


print(PairSum([2, 4, 7, 11, 14, 16, 20, 21], 31))
