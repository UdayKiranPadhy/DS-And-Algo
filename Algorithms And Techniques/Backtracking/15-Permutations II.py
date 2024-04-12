"""

https://leetcode.com/problems/permutations-ii/

47. Permutations II
Medium

8413

141

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        answer = set()

        def backtrack(rest_of_elements, picked):
            if len(picked) == N:
                answer.add(tuple(picked))
                return
            for i in range(len(rest_of_elements)):
                picked.append(rest_of_elements[i])
                backtrack(rest_of_elements[:i] + rest_of_elements[i+1:], picked)
                picked.pop()

        backtrack(nums,[])
        return [list(i) for i in answer]
