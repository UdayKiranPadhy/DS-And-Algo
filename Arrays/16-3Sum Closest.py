"""
15. 3Sum
Medium

10768

1088

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        solution = []
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    solution.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        solution = set(solution)
        solution = [list(x) for x in solution]
        solution.sort()
        return solution


model = Solution()
print(model.threeSum([-1, 0, 1, 2, -1, -4]))


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # a simple dfs is enough
#         l = len(nums)
#         if l < 3: return []

#         ans = []
#         def dfs(nums, cur, pos, target, d):
#             if d == 3:
#                 if target == 0:
#                     ans.append(cur.copy())
#                 return

#             for i in range(pos, l):
#                 cur.append(nums[i])
#                 dfs(nums, cur, i+1, target-nums[i], d+1)
#                 cur.pop()

#         dfs(nums, [], 0, 0, 0) # nums, cur, pos, depth
#         ans = set([tuple(sorted(x)) for x in ans])
#         return ans
