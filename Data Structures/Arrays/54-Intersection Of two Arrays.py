"""

349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Tags :
2Pointers Sorting Binary Search Hash Table 

"""

# Problem Statement
# https://leetcode.com/problems/intersection-of-two-arrays/

# Solution
# Since the answer contains only the common unique elements between two arrays,
# we can perform intersection operation .

# Complexity
# The Time Complexity is O(min(length of two sets)) in worst case its O(len(s)*len(t))
# where s and t are two sets. For more info https://wiki.python.org/moin/TimeComplexity#:~:text=Intersection s%26t,not a set
# The Space Complexity is linear O(1) as we didnt use any additional space .

# Code


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1, nums2 = set(nums1), set(nums2)
        return list(nums1.intersection(nums2))

# Follow up Hash Tables 3rd Question
