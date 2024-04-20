"""
https://leetcode.com/problems/largest-divisible-subset/description/


368. Largest Divisible Subset Solved Medium Topics Companies Given a set of distinct positive integers nums,
return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

"""

# Solution
# https://www.youtube.com/watch?v=bech4HH44Rs&t=223s&ab_channel=AlgorithmsMadeEasy


# TLE
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = defaultdict(list)

        def go(index, current):
            if index == N:
                ans[len(current)].append(current[:])
                return

            for i in range(index, N):
                error = False
                for num in current:
                    if nums[i] % num == 0 or num % nums[i] == 0:
                        continue
                    else:
                        error = True
                        break
                if not error:
                    go(i + 1, current + [nums[i]])
            ans[len(current)].append(current[:])

        go(0, [])
        return ans[max(ans.keys())][0]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        ans = [[]for i in range(N)]
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(ans[j]) > len(ans[i]):
                        ans[i] = ans[j][:]
            ans[i].append(nums[i])
        return max(ans,key=lambda a: len(a))


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp = [1] * N
        prev = [-1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        maximum = -float('inf')
        index = -1
        ans = []
        for i in range(N):
            if dp[i] > maximum:
                maximum = max(maximum, dp[i])
                index = i

        while index != -1:
            ans.append(nums[index])
            index = prev[index]
        return ans