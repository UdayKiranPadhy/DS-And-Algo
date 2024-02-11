"""

632. Smallest Range Covering Elements from K Lists
Hard
3.4K
63
Companies
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

"""
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mmax = -float('-inf')

        pq = []

        for i in range(len(nums)):
            heapq.heappush(pq, [nums[i][0], i , 0])
            mmax = max(mmax, nums[i][0])

        ans = [pq[0][0],mmax]

        while True:
            # element , k , index_
            poppedElement = heapq.heappop(pq)

            next_index = poppedElement[2] + 1

            if next_index == len(poppedElement[1]) -1:
                break

            next_element = [nums[poppedElement[1]][next_index], poppedElement[1], next_index]
            mmax = max(mmax, nums[poppedElement[1]][next_index] )

            heapq.heappush(pq,next_element)

            if mmax - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0],mmax]

        return ans

