"""
Sort an array of 0s, 1s and 2s 
Easy Accuracy: 51.36% Submissions: 44429 Points: 2
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2

Company Tags
 Adobe Amazon Hike MakeMyTrip MAQ Software Microsoft Morgan Stanley Ola Cabs OYO Rooms Paytm Qualcomm Samsung SAP Labs Snapdeal Walmart Yatra.com
Topic Tags
 Arrays Sorting
"""
# My Trail
def sort012(arr, N):
    low = 0
    high = len(arr) - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            continue
        if arr[mid] == 1:
            mid += 1
            continue
        if arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
            continue
