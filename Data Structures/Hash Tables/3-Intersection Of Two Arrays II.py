"""

350. Intersection of Two Arrays II
Easy

3061

565

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Tags :
2Pointers Sorting Binary Search Hash Table 

"""

# Problem statement
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Solution
# Similar to problem 0349 Intersection Of two arrays, but here we can use hash-table
# with number of occurrences or in python we can use Counter function. If our data is
# sorted, we can use two pointers approach, complexity will be O(m+n) and with
# additional O(1) memory, if we do not consider answer as memory. If one of arrays
# is much bigger than another, we can use binary search with complexity O(n log m).
# (note, that BS is quite tricky here, because we need to handle duplicates, we need
# to find the left-most matching number. Next time we perform binary search, the low
# should start from previously found index + 1). If nums2 is stored on disk, then we can
# put nums1 into hash table and use chunks of nums1. If nums1 is also big, we need to
# sort them, using external sort and use two pointers.

from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        counter = counter1 & counter2
        return list(counter.elements())
