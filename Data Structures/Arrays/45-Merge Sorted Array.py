"""

88. Merge Sorted Array
Easy

1206

136

Add to List

Share
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > 0 and nums1[-1] == 0:
            nums1.pop()
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        while len(nums1) != m + n:
            nums1.append(0)


# The Logic Is simple as last elements in nums1 are already 0's even if we replace them we wont lose data. And the data is being sorted in ascending order
# nums1 and nums2 are already sorted
# So,

# We compare last elements from both lists nums1 and nums2 and find the greatest and place it at last position of nums1
# Decrease m or n corresponding to the list that list in which you had greatest number at end and repeat step-1 and stop the loop when either m becomes 0 or n becomes 0
# a) When m > 0 it means that nums2 is alreeady merged in nums1. Hence nothing needs to be done.
# b) when n>0 it means that elements in nums2 that are remaining are all less that nums 1. Hence they can be directly rused to replace elements at the beginning of nums1

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        count = -1
        while(m > 0 and n > 0):
            if(nums1[m-1] > nums2[n-1]):
                nums1[count] = nums1[m-1]
                m -= 1
            else:
                nums1[count] = nums2[n-1]
                n -= 1
            count -= 1

        while(n > 0):
            nums1[count] = nums2[n-1]
            n -= 1
            count -= 1



"""
https://leetcode.com/problems/merge-sorted-array

Easy problem if you know the trick, but not so easy if you see this type of idea first time. Here we need to use two 
observations:

It is definitely 2 pointers approach, we need to iterate through nums1 and nums2 and build solution, using merge. 
Also, we need to start from end of our lists, and this is essential, if you start from the beginning of lists, 
you can accidentely rewrite you data, so you need to think where to put it first and it will be extra space. So, 
all we do is:

define p1 = m - 1 and p2 = n - 1: pointers for nums1 and nums2. We start from i = m + n - 1 and move in backward 
direction: we compare nums1[p1] and nums2[p2], write biggest number to nums1[i] and move one of the pointers: p1 or 
p2. This is not all: it can happen, that when we reached p1 = 0, there are still some numbers we need to copy from 
nums2 to nums1, and in next step we do this. Complexity: time complexity is O(n + m), space complexity is O(1): we 
did everything inplace."""

class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p1 < 0 or p2 < 0: break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1