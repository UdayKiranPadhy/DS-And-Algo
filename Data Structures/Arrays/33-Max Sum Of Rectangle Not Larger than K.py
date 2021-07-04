"""
Date :- 4/7/21
Source :- https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/


363. Max Sum of Rectangle No Larger Than K
Hard

1452

94

Add to List

Share
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

 

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).


Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3

Example 3:
[[2,2,-1]]
0

output = -1
 
Example 4:
Input:
[[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
10
Output:
10

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

Follow up: What if the number of rows is much larger than the number of columns?

"""


# Solution Model = https://www.youtube.com/watch?v=yCQN096CwWM&ab_channel=TusharRoy-CodingMadeSimple

import sys


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:

        def kaden(stack):
            max_ending_here = 0
            max_so_far = -sys.maxsize-1
            for i in stack:
                max_ending_here += i
                if max_ending_here < i:
                    max_ending_here = i
                max_so_far = max(max_ending_here, max_so_far)
            return max_so_far

        stack = [0]*len(matrix)
        maximum_sum = -sys.maxsize-1
        for l in range(len(matrix[0])):
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    stack[i] += matrix[i][r]
                for i in range(len(stack)):
                    current_sum = kaden(stack[i:])
                    if current_sum > maximum_sum and current_sum <= k:
                        maximum_sum = current_sum
            stack = [0]*len(matrix)
        return maximum_sum


model = Solution()
print(model.maxSumSubmatrix(
    [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10))
