"""

703. Kth Largest Element in a Stream
Easy

https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

"""


# Problem statement
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Solution
# Similar to Problems 0973 K Closest Points to Origin and 0215 Kth Largest Element in an Array
# with exactly the same idea: here we heap min-heap with k biggest elements,
# then k-th largest element will be in the root of our heap. When we have new
# element we check if it is more than root of our heap, then we put this element
# to heap and remove smallest element from heap, so we will always keep it k elements.

# Complexity
# It is O(k + (n-k)*log k) for init and O(log k) for add. Space complexity is O(k).

# Code
from heapq import heapify, heappushpop, heappush


class KthLargest:
    def __init__(self, k, nums):
        self.heap = nums[:k]
        heapify(self.heap)
        self.k = k
        for num in nums[k:]:
            if num > self.heap[0]:
                heappushpop(self.heap, num)

    def add(self, val):
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)

        return self.heap[0]
