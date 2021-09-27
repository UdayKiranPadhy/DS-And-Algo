"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

# Problem statement
# https://leetcode.com/problems/permutations/

from itertools import combinations
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        prem = set(permutations(nums))
        gg = []
        for i in prem:
            gg.append(list(i))
        return gg

# Additional Info


# Get all permutations of length 2
# and length 2
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
    print(i)


# A Python program to print all
# combinations of given length

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print(i)
