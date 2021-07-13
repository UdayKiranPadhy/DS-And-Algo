"""
Source :- GeeksForGeeks and also on Leetcode
https://leetcode.com/problems/two-sum/

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


# Soltuion
"""
There are different approaches to this problem: bruteforce with O(n^2), 
sorting of data + 2 pointers with O(nlogn) complexity.

Finally, we can use hash table to achieve O(n) complexity. The idea is for 
each number k try to find number target - k.

Complexity
Time complexity is O(n), however space complexity is also O(n). I think it is 
not possible to have O(n)/O(1) complexity solution.

"""

# Method - 1
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


# Solution-2
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i,num in enumerate(nums):
            check_num = target-num
            if check_num in d:
                return [i,d[check_num]]
            else:
                d[num]=i