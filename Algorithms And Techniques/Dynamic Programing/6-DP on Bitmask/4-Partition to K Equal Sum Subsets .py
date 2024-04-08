"""
Date :- 7/7/21
Link :- https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Partition to K Equal Sum Subsets
Medium

3257

202

Add to List

Share
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].


"""


# My initial trails
"""
I went in totally wrng way , not even realeated to question
"""




from functools import lru_cache
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        N = len(nums)
        sums = {}

        def go(mask, sum):
            if sum in sums and mask != 0:
                sums[sum] += 1
            elif mask != 0:
                sums[sum] = 1
            for i in range(N):
                if (mask & (1 << i) == 0):
                    go(mask ^ (1 << i), sum+nums[i])
        go(0, 0)
        print(sums)
        if k in sums.values():
            return True
        else:
            return False


# Right Solution
"""
    # 1. Check states that would make a solution impossible
    #    i.  max(nums) is greater than target
    #    ii. sum(nums) is not evenly divisible by k


    # 2. Find all sets of numbers that add to target value
    #    i.  t = sum of numbers used i.e. nums[1]+nums[2]+nums[4]        4 21
    #    ii. p = bit-masked path     i.e. nums[1], nums[2], nums[4] = '0b10110'


"""
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/817767/Python-3-steps-DFS-with-bit-masks

# Correct Solution
def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
    # 1. Check states that would make a solution impossible
    #    i.  max(nums) is greater than target
    #    ii. sum(nums) is not evenly divisible by k
    total = 0
    maxi = float('-inf')
    for n in nums:
        total += n
        maxi = max(n, maxi)

    if total % k: return False
    target = total // k
    if maxi > target:
        return False

    def bin_finder(i, t, p):
        nonlocal paths, nums

        if t == target:
            paths.append(p)
            return None

        if (t > target) or (i == len(nums)):
            return None

        bin_finder(i+1, t, p)
        bin_finder(i+1, t+nums[i], p|(1 << i))

    paths = []
    bin_finder(0, 0, 0)

    # 3. Every path in paths sums to the target value, find k paths that do not overlap
    #    i.e. for Example 1: nums = [4, 3, 2, 3, 5, 2, 1]
    #             paths = [[5],     [1,4],     [2,3],  [2,3]]
    #             paths = ['10000', '1000001', '1100', '100010'] when bitmasked using their indices
    #                        p1   |     p2     |  p3  |   p4  = '1111111'
    #             so every index was used (all ones) and each path sums to the target value
    target_path = (1 << len(nums)) - 1
    def path_finder(i, p):
        nonlocal res, paths

        if res: return None

        if p == target_path:
            res = True
            return None

        if i == len(paths):
            return None

        if not paths[i]&p:
            path_finder(i+1, p|paths[i])
        path_finder(i+1, p)

    res = False
    path_finder(0, 0)
    return res
