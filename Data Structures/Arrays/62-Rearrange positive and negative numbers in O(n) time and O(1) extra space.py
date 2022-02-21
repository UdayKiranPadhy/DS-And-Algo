# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/
"""

Rearrange positive and negative numbers in O(n) time and O(1) extra space
Difficulty Level : Medium

An array contains both positive and negative numbers in random order. 
Rearrange the array elements so that positive and negative numbers are 
placed alternatively. Number of positive and negative numbers need not be equal. 
If there are more positive numbers they appear at the end of the array. 
If there are more negative numbers, they too appear in the end of the array.
For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], 
then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]
Note: The partition process changes relative order of elements. 
I.e. the order of the appearance of elements is not maintained with 
this approach. See this for maintaining order of appearance of elements in this problem.


"""

# https://www.youtube.com/watch?v=zUPMACE0uBs&ab_channel=AyushiSharma

# Step - 1 Seperate Negative and positive integers at the ends of the array by two pointer approach
# Step - 2 rearrange it now


def rearrange(arr, n):
    i = 0
    j = n - 1

    # shift all negative values
    # to the end
    while (i < j):

        while (i <= n - 1 and arr[i] > 0):
            i += 1
        while (j >= 0 and arr[j] < 0):
            j -= 1

        if (i < j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # i has index of leftmost
    # negative element
    if (i == 0 or i == n):
        return 0

    # start with first positive element
    # at index 0

    # Rearrange array in alternating
    # positive & negative items
    k = 0
    while (k < n and i < n):

        # swap next positive element at even
        # position from next negative element.
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp
        i = i + 1
        k = k + 2
