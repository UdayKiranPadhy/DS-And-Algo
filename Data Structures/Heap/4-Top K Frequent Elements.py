"""

347. Top K Frequent Elements
Medium

6250

301

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

# https://leetcode.com/problems/top-k-frequent-elements

# There are solution, using quickselect with O(n) complexity in average, but I think
# they are overcomplicated: actually, there is O(n) solution, using bucket sort.
# The idea, is that frequency of any element can not be more than n. So, the plan is
# the following:

# Create list of empty lists for bucktes: for frequencies 1, 2, …, n.
# Use Counter to count frequencies of elements in nums
# Iterate over our Counter and add elements to corresponding buckets.
# buckets is list of lists now, create one big list out of it.
# Finally, take the k last elements from this list, these elements will be top K frequent elements.
# Complexity: time complexity is O(n), because we first iterate over nums once and create buckets, then we flatten list of lists with total number of elements O(n) and finally we return last k elements. Space complexity is also O(n).

from heapq import heappop, heapify
from collections import ChainMap
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()
        for num, freq in Count:
            bucket[freq].append(num)
        flat_list = list(ChainMap(*bucket))
        return flat_list[::-1][:k]


# Heap Implementation


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = [[-count[i], i] for i in count]
        heapify(maxHeap)
        ans = []
        while k:
            ans.append(heappop(maxHeap)[1])
            k -= 1
        return ans
