from functools import cache
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)

        def go(index, total):
            maximum = -float('inf')
            if total % 3 == 0:
                maximum = total

            if index >= N:
                return max(maximum,-float('inf'))

            take = go(index + 1, total + nums[index])
            skip = go(index + 1, total)
            return max(maximum, take, skip)

        return go(0, 0)


model = Solution()
print(model.maxSumDivThree([3, 6, 5, 1, 8]))  # 18
