"""

Next Permutation
Medium

6835

2235

Add to List

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100


"""


# Problem Statement
# https://leetcode.com/problems/next-permutation/

# Summary
# We need to find the next lexicographic permutation of the given list of numbers than the 
# number formed by the given array.

# Solution
# Approach 1: Brute Force
# Algorithm

# In this approach, we find out every possible permutation of list formed by the elements 
# of the given array and find out the permutation which is just larger than the given one. 
# But this one will be a very naive approach, since it requires us to find out every possible 
# permutation which will take really long time and the implementation is complex. Thus, this 
# approach is not acceptable at all. Hence, we move on directly to the correct approach.

# Complexity Analysis

# Time complexity : O(n!). Total possible permutations is n!.
# Space complexity : O(n). Since an array will be used to store the permutations.

# Approach 2: Single Pass Approach
# Example [1,5,8,4,7,6,5,3,1]
# 1) Traverse from the right towards left until u find a decresing element
#    [7,6,5,3,1] is increasing but next element got decreased so mark that '4' with one pointer
# 2) Traverse to right from the pointer until u find an element just greater than '4'
#    [7,6, 5 ,3,1] 5 it the next greater element 
# 3) Swap 5 and 4 
#     [1,5,8,5,7,6,4,3,1]
# 4) Now reverse all the elements from 7 to last
#     [1,5,8,5,1,3,4,6,7]
# This problem is very similar to problem 556. Next Greater Element III, with 
# exactly the same reasoning:

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(L,start,end):
            while start < end:
                L[start] , L[end] = L[end] , L[start]
                start +=1
                end += 1

        i , n = len(nums) - 1 , len(nums)

        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i != 0:
            j = i
            while j+1 < n and nums[j+1] > nums[j]:
                j+=1
            
            nums[i-1] , nums[j] = nums[j] , nums[i-1]

        reverse(nums, i ,n-1)
