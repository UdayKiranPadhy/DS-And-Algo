"""

90. Subsets II
Medium

4602

142

Add to List

Share
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

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
