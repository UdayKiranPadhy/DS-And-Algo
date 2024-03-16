from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)

        ones = {}
        zeros = {}

        for i in range(N):
            ones[i] = strs[i].count('1')
            zeros[i] = strs[i].count('0')

        @cache
        def go(index, m, n):
            if index >= N:
                return 0
            if m < 0 or n < 0:
                return 0
            op1 = -float('inf')
            if zeros[index] <= m and ones[index] <= n:
                op1 = 1 + go(index + 1, m - zeros[index], n - ones[index])
            op2 = go(index + 1, m, n)
            return max(op1, op2)

        return go(0, m, n)

model = Solution()
print(model.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))  # 4