"""

Three way partitioning

Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Note: The generated output is 1 if you modify the given array successfully.


Example 1:

Input:
n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.


Example 2:

Input:
n = 3
A[] = {1, 4, 3, 6, 2, 1}
[a, b] = [1, 3]
Output: 1
Explanation: One possible arrangement
is: {1, 3, 2, 1, 4, 6}. If you return a valid
arrangement, output will be 1.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)


Constraints:
1 <= n <= 106
1 <= A[i] <= 106


"""


# a0, a1 ...... .. .. . . an
# 0 - low-1                     0    <a
# low - (mid -1)                1     a - b
# mid - (high -1) Unsorted
# high - n                      2     b >

class Solution:
    def threeWayPartition(self, array, a, b):
        N = len(array)
        low = mid = 0
        high = N - 1

        while mid < high + 1:
            if array[mid] < a:
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
                continue
            if a <= array[mid] < b:
                mid += 1
                continue
            else:
                array[high], array[mid] = array[mid], array[high]
                high -= 1
                continue

        return array

model = Solution()
print(model.threeWayPartition([76,8,75,22,59,96,30,38,36],44,62))
