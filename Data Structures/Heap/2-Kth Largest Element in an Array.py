"""

Kth Largest Element in an Array
Medium

7104

412

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

"""


from heapq import heapify, heappop
import random
from typing import List

# https://leetcode.com/problems/kth-largest-element-in-an-array

# If you see this problem in competition, the best way just to sort data and choose 
# k-th largest element in O(n log n) overall complexity. However you can imagine, 
# that it is not the good idea for real interview, where your expected do do something else. 
# There is two classical ways how to find order statistic in linear time (yes, it has its 
# mathematical name):

# Median of median approach with worst time complexity O(n), however it is quite painful 
# to code and I do not think anyone expect that you do it.
# So-called Quick Select, which use similar idea to Quick Sort, with average complexity O(n).
# We are going to discuss Quick Select, because it is easier to code:

# First, we need to choose so-called pivot and partition element of nums into 3 parts: elements, 
# smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: 
# less and more or equal)
# Next step is to see how many elements we have in each group: if k <= L, where L is 
# size of left, than we can be sure that we need to look into the left part. 
# If k > L + M, where M is size of mid group, than we can be sure, that we need to look 
# into the right part. Finally, if none of these two condition holds, we need to look in 
# the mid part, but because all elements there are equal, we can immedietly return mid[0].
# Complexity: time complexity is O(n) in average, because on each time we reduce searching 
# range approximately 2 times. This is not strict proof, for more details you can do some 
# googling. Space complexity is O(n) as well.

class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [x*-1 for x in nums]
        heapify(maxHeap)
        while k != 0:
            value = heappop(maxHeap)
            k -= 1
        return value*-1
