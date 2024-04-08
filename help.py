import string
from bisect import bisect_left
from typing import List

bisect_left
#
#
# class Solution:
#     def longestMonotonicSubarray(self, nums: List[int]) -> int:
#         N = len(nums)
#         if N == 1:
#             return 1
#         prev = [(1, 0)] * N
#         best = -float('inf')
#         for i in range(1, N):
#             if nums[i] > nums[i - 1]:
#                 if prev[i - 1][1] >= 0:
#                     prev[i] = (prev[i - 1][0] + 1, 1)
#                 elif prev[i-1][1] < 0:
#                     prev[i] = (2, 1)
#             elif nums[i] < nums[i - 1]:
#                 if prev[i - 1][1] <= 0:
#                     prev[i] = (prev[i - 1][0] + 1, -1)
#                 elif prev[i-1][1] > 0:
#                     prev[i] = (2, -1)
#             best = max(best,prev[i][0])
#         return best


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = ""
        mappings = {}
        for idx, value in enumerate(string.ascii_lowercase):
            mappings[idx] = value

        def distance(char1, char2):
            if char1 == char2:
                return 0
            op1 = float('inf')
            if chr(ord(char1) - 1) >= 'a':
                op1 = 1 + distance(chr(ord(char1) - 1), char2)
            return op1

        for char in s:
            position = ord(char) - ord('a')
            mini = char
            for number in range(1,min(k+1, 25)):
                new_char = mappings[(position + number) % 26]
                mini = min(mini, new_char)
                if position - number >= 0:
                    new_char = mappings[(position - number) % 25]
                    mini = min(mini, new_char)
            dis = distance(char, mini)
            k = k - min(dis, 26 - dis)
            result += mini
        return result

model = Solution()
print(model.getSmallestString("zbbz", 3))
