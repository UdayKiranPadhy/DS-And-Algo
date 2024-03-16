from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = list(freq.items())
        nums.sort()
        N = len(nums)

        def go(index: int):
            if index >= N:
                return 0
            # Take the current number
            score = nums[index][0] * nums[index][1]
            if index + 1 < N and nums[index + 1][0] != nums[index][0] + 1:
                op1 = score + go(index + 1)
            else:
                op1 = score + go(index + 2)
            # Skip the current number
            op2 = go(index + 1)
            return max(op1, op2)

        return go(0)