from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for i in range(len(nums)):
            if nums[i] > nums[max2]:
                max1 = max2
                max2 = i
                continue
            if nums[i]> nums[max1]:
                max1 = i
                continue
        return (nums[max2] - 1) * (nums[max1] - 1)


model = Solution()
gg = model.maxProduct([1, 5, 4, 5])
print(gg)
