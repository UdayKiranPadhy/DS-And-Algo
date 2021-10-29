"""

373. Find K Pairs with Smallest Sums
Medium

2480

151

Add to List

Share
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000


"""

# Problem statement
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# Solution
# There is bruteforce solution with O(mn * log(mn)) complexity.

# We can do better: let us denote xi,j=nums1[i]+nums2[j] - we are not going to
# evaluate all sums, we do it just for simpler notations. On the first step put
# numbers x0,0,…,xn−1,0 into heap: first elements in each row. Then at each iteration
# we find the smallest element, remove it, and put the next element in given row, for
# example remove x3,0 and put x3,1. At any moment of time we have elements x0,i0,…,xn−1,in−1
# in our heap, that is one element from each row (actually ⩽1 element, if row is finished).
# Also, if k<n, we can consider only first k rows.

# Complexity
# Time complexity is O(n+klogn), for k>n and O(klogk) for k<n. We can keep only the second
# complexity, because logn and logn2 differ only 2 times.

# Code

from heapq import *


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        n1, n2 = len(nums1), len(nums2)
        heap = [(num + nums2[0], i, 0) for i, num in enumerate(nums1)]
        heapify(heap)
        result = []

        for _ in range(min(k, n1*n2)):
            num, ind1, ind2 = heappop(heap)
            result.append([nums1[ind1], nums2[ind2]])
            if ind2 < n2 - 1:
                heappush(heap, (nums1[ind1] + nums2[ind2+1], ind1, ind2+1))

        return result
