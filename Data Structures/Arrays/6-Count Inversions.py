"""
Count Inversions 
Easy 
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.
Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*105
1 ≤ arr[i] ≤ 1018

Company Tags
 Adobe Amazon BankBazaar Flipkart Microsoft Myntra
Topic Tags
 Arrays Sorting Divide and Conquer
"""
from typing import List

# HInt 1
"""
A naive solution to this would be to use 2 nested for-loops and for every index i, find the count of elements greater than arr[i] to the right of it. Finally, return the sum of such counts for every value of 0 <= i < n. 

But the time complexity of this will be O(n2). Can we make it better? 
"""

# Hint 2
"""
We basically need to make the comparisons in the existing array and while doing any comparison, we need to know that how would the two numbers being compared would be ordered in the sorted version of this array.
So, how about running a sorting algorithm itself?
The algorithms like Bubble Sort, Insertion Sort and Selection sort are O(n2). We can achieve this complexity even via the naive approach discussed in the previous hint, so no use of it.

What about getting to this via merge sort?
"""

# Hint 3
"""
Use Merge sort algorithm, and sort the array.
In merge function for merge sort, while comparing the elements, if element in right array is smaller, then it is an inversion (Why..??)
This means that this smaller element in the original array, is behind larger elements. So add the number of larger elements or elements left in the left-array, to the value of counter.
This process is repeated again and again for complete Merge Sort
Finally output counter variable. This is the answer.
"""


# Counting Inversions but not n^2 it is need to done with nlogn complexity so its a modified merge sort


def merge(arr: List[int], low: int, mid: int, high: int) -> int:
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    cnt = 0  # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Modification 2
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt  # Modification 3


def mergeSort(arr: List[int], low: int, high: int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    return cnt


def numberOfInversions(a: List[int], n: int) -> int:
    # Count the number of pairs:
    n = len(a)
    # Count the number of pairs:
    return mergeSort(a, 0, n - 1)
