"""

1218. Longest Arithmetic Subsequence of Given Difference
Attempted
1597
Medium
Topics
Companies
Hint
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].


Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104

"""
import bisect
from collections import defaultdict
from functools import cache
from typing import List


# My initial Trials
# Failed
# TC -> 10^5 * 10^4
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)

        @cache
        def go(index, prev):
            if index == -1:
                return 0
            if prev is None:
                return max(1 + go(index - 1, arr[index]), go(index - 1, None))
            elif prev - difference == arr[index]:
                return 1 + go(index - 1, arr[index])
            else:
                return go(index - 1, prev)

        return go(N - 1, None)


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        indexes = defaultdict(list)
        for idx, value in enumerate(arr):
            indexes[value].append(idx)
        N = len(arr)

        @cache
        def go(idx):
            if idx == N:
                return 0
            next = arr[idx] + difference
            ans = 1
            next_index = bisect.bisect_left(indexes[next],idx+1)
            if next_index != len(indexes[next]):
                ans += go(indexes[next][next_index])
            return ans

        return max(go(i) for i in range(N))


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for num in arr:
            if num - difference in dp:
                dp[num] = 1 + dp[num-difference]
            else:
                dp[num] = 1
        return max(dp.values())

model = Solution()
print(model.longestSubsequence([1,2,3,4],1))
