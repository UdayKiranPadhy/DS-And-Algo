"""

90. Subsets II
Medium

https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""


# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


# Complexity
# Not very tight bound for time complexity is O(2^n*n), where n is total number
# of elements, space complexity as well. In fact complexity (time and space)
# is O((a1+1)*...*(ak+1)*n), where a1, ..., ak are frequencies of each element.


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(index, subset):
            if index >= len(nums):
                res.append(subset[::])
                return

            # Take the number
            subset.append(nums[index])
            backtrack(index+1, subset)
            subset.pop()

            # Dont take that number
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, subset)

        backtrack(0, [])
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        N = len(nums)
        for mask in range(1 << N):
            current = []
            for index in range(N):
                if mask & (1 << index) > 0:
                    current.append(nums[index])

            subsets.add(tuple(sorted(current)))

        return subsets
