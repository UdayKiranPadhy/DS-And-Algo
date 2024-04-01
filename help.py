from itertools import accumulate
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        count = 0
        prev = None
        gg = []
        for right in range(N):
            if prev == None:
                prev = nums[right]
                count += right - left + 1
                gg.append(1)
                continue
            if prev == nums[right]:
                left = right
            count += right - left + 1
            prev = nums[right]
            gg.append(right - left + 1)

        print(gg)
        return count

model = Solution()
print(model.countAlternatingSubarrays([1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])) #76