"""

Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first 
index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

"""

# Approach 1
# Being Greedy is rewarding sometimes


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for index, value in enumerate(nums):
            if index > farthest:
                return False
            farthest = max(farthest, index+value)
        return True

# Approach 2
# The trick with these kind of problems is :

# Solve it with brute force.
# Do with recursive back-tracking.
# Go with dynamic programming where you analyze each step of what you do.
# Optimize with memoization.
# Further reduce the run time when you see the pattern and apply greedy algorithm.
# For this problem when we realise we only have to travel towards the end of the array,
# we can figure out how to use greedy approach. Instead of reaching the last position
# from the starting index, we try to find out if we can reach a good index that will
# have a path leading to the last index. Lets call this as lastBestPos . The last index
# is ofcourse always the lastBestPos at the beginning. Then we decrease the index number
# and check if from there we can go to the lastBestPos if so, this becomes our new
# lastBestPos as we know there already exists the path from here to the last index.
# And we continue so on, until we reach the starting index of the array.

# If we reach the first index while looping backwards through the array, we return True ,
# else, we return False.


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        lastBestPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (i+nums[i] >= lastBestPos):
                lastBestPos = i
        return lastBestPos == 0
# Time Complexity : O(n) -- We are doing a single pass for loop in the array having 
# n(length of the nums array) steps.
# Space Complexity : O(1) -- No extra memory used.


# Idea:
# Consider nums[i] to be the amount of fuel in the tank sitting at i that we can 
# switch to. As moving from left to right, we lose 1 unit of fuel per step. At 
# each index, we switch to the new tank if it has more fuel than what we have left. 
# If the amount of fuel goes to zero somewhere in the middle, return False.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        fuel = 0
        for i in range(len(nums)-1):
            fuel = max(fuel, nums[i])
            if fuel == 0:
                return False
            fuel -= 1
        return True


# https://leetcode.com/problems/jump-game/discuss/1500036/Being-Greedy-is-rewarding-sometimes-or-Easy-To-Understand-or-Concise