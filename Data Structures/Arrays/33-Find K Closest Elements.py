"""
Date :- 2 July 2021
Source :- Leetcode
https://leetcode.com/problems/find-k-closest-elements/description/

658. Find K Closest Elements
Given a sorted integer array arr, two integers k and x, return 
the k closest integers to x in the array. The result should also 
be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104



"""

# Solution Approach 1
# Sort by distance from x
"""
In this approach, we can take the given input array and sort its elements by their distance from x. 
After sorting we can choose the first k elements and then return them after sorting in ascending order. 
One point to note that we must use stable sort to ensure that 2nd condition given in the question is satisfied.
"""


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        arr.sort(key=lambda g: abs(g-x))
        arr = arr[:k]
        arr.sort()
        return arr


"""
Time Complexity : O(nlogn + klogk), where n is the number of elements in arr and k is the 
number of closest element to be chosen. First we require O(nlogn) to custom-sort the whole array, 
then we are choosing the first k elements and sorting them in ascending order which takes another O(klogk).
Space Complexity : O(1) only constant space is required (ignoring the space used by in-built sorting algorithms)
"""


# Solution Approach 2
# 2-Pointers
"""
We can initialize two pointers L=0 and R=n-1. Now our window size is n and 
contains excess elements. 
We will keep reducing the [L, R] window size till it becomes exactly equal to k. 
We can do this based on the condition - x - arr[L] <= arr[R] - x. 
If it is true, then it means arr[R] is farther away from x than arr[L] and thus we 
will eliminate arr[R]. Otherwise, we will eliminate arr[L].
"""


class Solution2:
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr)-1
        while r-l != k and r > l:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        if r > l:
            return arr
        return arr[l:r]


"""
Time Complexity : O(n-k), we will keep reducing the window size from initial n to final k which will require a total of n-k comparisons.
Space Complexity : O(1)
"""


# Solution Approach 3:
# Binary Search And 2 Pointers
"""
In the above approaches, we are not taking any advantage of the fact that input array 
given to us is already sorted. We can use binary search to find the smallest element 
in arr which is greater or equal to x. Let's mark this index as R. Let's mark the index 
preceding to R as L and element at this index will be smaller than x

Now, [L, R] forms our window of elements closest to x. We have to expand this window 
to fit k elements. We will keep picking either arr[L] or arr[R] based on whichever's 
closer to x and expand our window till it contains k elements.


Time Complexity : O(logn + k), We need O(logn) time complexity to find r at the start. Then we need another O(k) time to expand our window to fit k elements
Space Complexity : O(1)
"""

# Solution Approach 4:
# Modified Binary Search and 2 pointers
"""
We can see that the answer would always be an array of k elements. 
So, the left pointer L must always start atleast k positions from the end, 
otherwise we would not have enough elements for our answer. So, instead of doing 
binary search on the entire arr, we could just do a binary search on [0, n-k] indices of arr.

Here, R won't always hold the index of smallest elmeent >= x as it did above but rather it 
holds index of some element that we are sure would be part of the final window. Thereafter, the 
process will remain the same of above - use 2-pointers to fit k elements inside our window.

Time Complexity : O(log(n-k) + k), We need O(logn) time complexity to find r at the start. Then we need another O(k) time to expand our window to fit k elements
Space Complexity : O(1)
"""

class Solution:
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) / 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]


# Solution - V (Modified Binary Search to find L)
"""
We can also observe that the answer will always be a continuous sub-array of arr. 
In the above approach we used binary search to find index of some element that would surely be 
part of our final window. We can further modify our approach to instead use binary search to 
find the left bound of our window so that we could eliminate the need for 2-pointers altogether.

Here, we will initialize L = 0 and R = n-k (<- using the solution - IV optimization here). We 
have mid = (L+R)/2. Now, consider arr[mid] and arr[mid + k]. Both of these elements surely can't be 
in our final answer or else the final array size exceeds k. So we have to pick one of these.

If arr[mid] is closer to x, then we will never pick arr[mid+k] or any element to its right in 
our final answer - so we can safely eliminate those elements and update R = mid.
If arr[mid + k] is closer to x, then we will never pick arr[mid] or any elements to its left 
in our final answer - so we can safely eliminate those elements and update L = mid + 1.
"""

arr = [int(x) for x in input().split(" ")]
k = int(input())
x = int(input())

model = Solution2()
print(*model.findClosestElements(arr, k, x))
