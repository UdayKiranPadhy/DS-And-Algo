"""
Link :- https://leetcode.com/problems/partition-equal-subset-sum/
Date :- 11/6/21

416. Partition Equal Subset Sum
Medium

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


"""

from functools import lru_cache


class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        @lru_cache(None)
        def KnapSack(index, sum):
            if sum == 0:
                return True
            elif index == 0 and sum != 0:
                return False
            elif nums[index-1] <= sum:
                return KnapSack(index-1, sum-nums[index-1]) or KnapSack(index-1, sum)
            else:
                return KnapSack(index-1, sum)

        if sum(nums) % 2 == 0:
            return KnapSack(len(nums), int(sum(nums)/2))
        else:
            return False


model = Solution()
print(model.canPartition([1, 5, 10, 6]))
