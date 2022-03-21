"""

Problem Link:-https://leetcode.com/problems/array-of-doubled-pairs/

954. Array of Doubled Pairs

Given an array of integers arr of even length, return true if and only if it is 
possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for 
every 0 <= i < len(arr) / 2.

Example 1:

Input: arr = [3,1,3,6]
Output: false


Example 2:

Input: arr = [2,1,2,6]
Output: false


Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
Input: arr = [1,2,4,16,8,4]
Output: false
 
Constraints:

0 <= arr.length <= 3 * 10^4
arr.length is even.
-10^5 <= arr[i] <= 10^5

"""


# Trails
"""
My Solution

Sort the array and then for every element x in the array do a Binary Search for 2*x in the 
array.
"""

# Fails with out Binary Search for last and large inputs
def canReorderDoubled(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arr.sort()
    while len(arr) != 0:
        number = arr[0]
        if number < 0:
            number_to_find = number / 2
        else:
            number_to_find = number * 2
        if number_to_find in arr:
            arr.remove(number_to_find)
            arr.pop(0)
        else:
            return False
    else:
        return True


# Failed Some cases
from bisect import bisect_left


def canReorderDoubled(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arr.sort()
    while len(arr) != 0:
        number = arr[0]
        if number < 0:
            number_to_find = number / 2
        else:
            number_to_find = number * 2
        gg = bisect_left(arr, number_to_find)
        if gg != len(arr) and arr[gg] == number_to_find:
            arr.pop(0)
            arr.remove(number_to_find)
        else:
            return False
    else:
        return True
