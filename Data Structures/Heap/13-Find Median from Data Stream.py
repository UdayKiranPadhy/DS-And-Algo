"""

295. Find Median from Data Stream
Hard

https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""

# Problem statement
# https://leetcode.com/problems/find-median-from-data-stream/

# Solution
# The idea is to keep two heaps: one for the top half of our data and another is for down 
# half of our data. If we have even size 2n, then we will keep two heaps with size n If we 
# have odd size 2n+1, then we will keep size of the small heap n+1 ans the size of large heap n.
# The small heap can be a max heap and the larger be a min heap.

# When we have new element num, we always put it to small heap, and then normalize our 
# heaps: remove biggest element from the small heap and put it to the large heap. After 
# this operation we can be sure that we have the property that the largest element in small 
# heap is smaller than smaller elements in large heap.

# However after this step if we had n,n elements, we will have n,n+1 elements, so we need to 
# put one element from large heap to small heap.

# Complexity
# Time complexity is just O(1) to get median and O(logn) to add number. 
# Space complexity is O(n) after n operations.

# Code
from heapq import * 
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], [] 

    def addNum(self, num):
        heappush(self.small, -num)           
        heappush(self.large, -heappop(self.small))
        
        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))
            
    def findMedian(self):
        if len(self.large) != len(self.small):
            return -self.small[0]                  
        else:
            return (self.large[0] - self.small[0]) / 2 

# Remark
# There is also solution with O(logn) time complexities for both operations, 
# if we use Sorted List

model = MedianFinder()

model.addNum(5)
model.addNum(4)
model.addNum(-1)
model.addNum(2)
model.addNum(4)
model.addNum(7)
model.addNum(-8)
model.addNum(9)

print(model.findMedian())



# A much easy to understand code
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small,-num)
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = heappop(self.small)
            heappush(self.large,-val)
        if len(self.small) > len(self.large) + 1:
            val = heappop(self.small)
            heappush(self.large,-val)
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()