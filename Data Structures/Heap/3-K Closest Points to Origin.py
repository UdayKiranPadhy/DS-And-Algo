"""

K Closest Points to Origin
Medium


Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).
 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 10^4
-10^4 < xi, yi < 10^4

"""

from typing import List
from heapq import heapify, heappop

# When you see in the statement of the problem that you need you find k biggest or k
# smallest elements, you should immediately think about heaps or sort. Here we need
# to find the k smallest elements, and hence we need to keep max heap. Why max and
# not min? We always keep in the root of our heap the k-th smallest element. Let us
# go through example: points = [[1,2],[2,3],[0,1]], [3,4], k = 2.

# First we put points [1,2] and [2,3] into our heap. In the root of the heap we have
# maximum element [2,3]
# Now, we see new element [0,1], what should we do? We compare it with the root, see,
# that it is smaller than root, so we need to remove it from our heap and put new
# element instead, now we have elements [1,2] and [0,1] in our heap, root is [1,2]
# Next element is [3,4] and it is greater than our root, it means we do not need to do anything.


# Complexity
# We process elements one by one, there are n of them and push it into heap and
# pop root from our heap, both have O(log k) complexity, so finally we have
# O(n log k) complexity, which is faster than O(n log n) algorighm using sorting.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return pow(x, 2)+pow(y, 2)
        minHeap = [[distance(x, y), [x, y]] for x, y in points]
        heapify(minHeap)
        ans = []
        while k:
            ans.append(heappop(minHeap)[1])
            k -= 1
        return ans


# Solution 2:
# Even though this algorighm has not optimal algorithmic complexity (it is O(n log n) vs
# heaps O(n log k), on leetcode it can work faster. Just sort points by distances and
# choose the smallest K of them

class Solution:
    def kClosest(self, points, K):
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:K]
