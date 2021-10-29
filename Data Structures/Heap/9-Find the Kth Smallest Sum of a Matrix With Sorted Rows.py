"""

1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
Hard

685

8

Add to List

Share
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

 

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
 

Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.

"""

# Problem statement
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

# Solution 1
# The idea is to keep heap, where we keep tuple (sum, i1, ... i_{m-1}): total sum and
# indexes of elements from each row. When we extract new element, we add m new candidates.

# Complexity
# We can have upto O(m*k) element in our heap in the end, because we add m elements
# on each step. Size of each element is O(n), so one extraction will be O(log(mk)*O(n))
# and O(nk*log(mk)) for all extractions. Also we do a lot of pushes, m times bigger,
# so we have O(nmk*log(mk)) complexity. There is also time for working with tuples,
# which iteration it is O(mn), so total factor O(mnk) will be smaller. Final time
# complexity is O(mnk*log(mk)). Space complexity is O(mnk). Factor log(mk) can be
# reduced to log(k) if we keep size of heap no more than k.

# Code
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        nrow, ncol = len(mat), len(mat[0])

        smallest = sum([mat[i][0] for i in range(nrow)])

        choice = [smallest] + [0]*(nrow)
        seen = set()
        pq = [choice]

        while k-1:

            prev = heappop(pq)
            k -= 1
            for i in range(nrow):

                if prev[i+1] == ncol-1:
                    continue

                next_ = prev.copy()
                next_[0] -= mat[i][next_[i+1]]
                next_[i+1] += 1
                next_[0] += mat[i][next_[i+1]]

                if tuple(next_) in seen:
                    continue

                heappush(pq, (next_))
                seen.add(tuple(next_))
        return pq[0][0]


# Solution 2
# See similar problem 0373 Find K pairs with smallest sums(11 in this folder). Actually we can apply it several times.

# Complexity
# Time complexity will be O(k*log k*m).


class Solution:
    def kthSmallest(self, mat, k):
        def kSmallestPairs(nums1, nums2, k):
            if not nums1 or not nums2:
                return []
            n1, n2 = len(nums1), len(nums2)
            heap = [(num + nums2[0], i, 0) for i, num in enumerate(nums1)]
            heapify(heap)
            result = []

            for _ in range(min(k, n1*n2)):
                num, ind1, ind2 = heappop(heap)
                result.append(nums1[ind1] + nums2[ind2])
                if ind2 < n2 - 1:
                    heappush(heap, (nums1[ind1] + nums2[ind2+1], ind1, ind2+1))

            return result

        m, n = len(mat), len(mat[0])
        res = mat[0]
        for i in range(1, m):
            res = kSmallestPairs(res, mat[i], k)
        return res[k-1]
