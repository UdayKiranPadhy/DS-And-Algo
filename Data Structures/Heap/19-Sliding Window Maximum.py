"""

239. Sliding Window Maximum
Hard

https://leetcode.com/problems/sliding-window-maximum/submissions/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

"""


from heapq import heapify
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        maxHeap = [(-element, index) for index, element in enumerate(nums[:k])]
        heapify(maxHeap)
        seen = set()
        ans.append(-maxHeap[0][0])
        seen.add(0)
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while maxHeap and maxHeap[0][1] in seen:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])
            seen.add(i-k+1)
        return ans
