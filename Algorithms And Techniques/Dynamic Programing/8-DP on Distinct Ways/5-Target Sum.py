"""
Link :- https://leetcode.com/problems/target-sum/
Date :- 10/9/21

494. Target Sum
Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1

Example 3:
Input: nums = [0,0,0,0,0,0,0,1], target = 1
Output: 128

Example 4:
Input: nums = [1,0], target = 1
Output: 2

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000


"""


# Methods used by knapsack variation
# My Trails Not successed due to some testcase
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def countSubsets(i, sum):
            if sum < 0:
                return 0
            if sum == 0:
                return 1
            if i == 0 and sum != 0:
                return 0
            elif nums[i-1] <= sum:
                return countSubsets(i-1, sum-nums[i-1]) + countSubsets(i-1, sum)
            else:
                return countSubsets(i-1, sum)

        subset = (sum(nums) + target) / 2
        return countSubsets(n, subset)


# My Trails 2 Failed for cases like [1,0] target = 1
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def countSubsets(i, sum):
            if sum < 0:
                return 0
            if sum == 0:
                return 1
            if i == n and sum != 0:
                return 0
            elif nums[i] <= sum:
                return countSubsets(i+1, sum-nums[i]) + countSubsets(i+1, sum)
            else:
                return countSubsets(i+1, sum)

        subset = (sum(nums) + target) / 2
        return countSubsets(0, subset)


# Non KnapSack Varitation
# Finally succeded my trails
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        N = len(nums)

        @lru_cache(None)
        def go(index, target):
            if index == N and target == 0:
                return 1
            elif index == N and target != 0:
                return 0
            op1 = nums[index] + go(index + 1, target - nums[index])
            op2 = -nums[index] + go(index + 1, target + nums[index])
            return (op1+op2)

        return go(0, target)
