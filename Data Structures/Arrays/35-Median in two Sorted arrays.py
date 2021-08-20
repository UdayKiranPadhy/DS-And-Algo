"""

4. Median of Two Sorted Arrays
Hard

11853

1651

Add to List

Share
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""

#  Didnt work


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        N = len(nums1)
        M = len(nums2)
        mid2 = False
        if (N+M) % 2 == 0:
            mid1 = (N+M)//2
            mid2 = (N+M)//2 + 1
        else:
            mid1 = (N+M)//2

        sorted = []
        n1 = 0
        m1 = 0
        if mid2:
            while len(sorted) < mid2:
                if nums1[n1] < nums2[m1]:
                    sorted.append(nums1[n1])
                    n1 += 1
                else:
                    sorted.append(nums2[m1])
                    m1 += 1
            poped1 = sorted.pop()
            poped2 = sorted.pop()
            return (poped1 + poped2) / 2
        else:
            while len(sorted) < mid1:
                if nums1[n1] < nums2[m1]:
                    sorted.append(nums1[n1])
                    n1 += 1
                else:
                    sorted.append(nums2[m1])
                    m1 += 1
            return sorted.pop()


# not so efficient in term of memory, but it works.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()

        if len(nums1) % 2 == 0:
            index = (len(nums1)-1) // 2
            return (nums1[index] + nums1[index+1]) / 2
        else:
            index = len(nums1) // 2
            return nums1[index]
