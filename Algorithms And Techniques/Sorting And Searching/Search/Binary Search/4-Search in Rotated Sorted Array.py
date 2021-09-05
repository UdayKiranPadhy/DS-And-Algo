"""

Search in Rotated Sorted Array
Medium

9455

737

Add to List

Share
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104



"""

# The rotated array can be thought as a composition of two arrays as the picture below shows. 
# We first selected the middle element and we have to figure in which part of the array we are in. 
# If the nums[mid]>=nums[start], then we are in the red part. If not, we are in the blue part.

# See image

# If we are in the red zone we know that the elements in the range [start, mid] are bounded 
# below by nums[start] and are bounded above by nums[mid]. If target is in this range, then 
# it must be located between start and mid so we update the end pointer to point to mid-1. 
# If it is not within this range, then we can disregard every element in the range [start, mid] 
# and we can update the start pointer to point to mid+1. A similar argument works if we 
# happen to be in the blue zone.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            ind = start + (end-start)//2
            if nums[ind] == target:
                return ind
            
            if nums[ind] >= nums[start]:
                if nums[start] <= target < nums[ind]:
                    end = ind - 1
                else:
                    start = ind + 1
            
            else:
                if nums[ind] < target <= nums[end]:
                    start = ind + 1
                else:
                    end = ind - 1
            
            
        return -1



model = Solution()
print(model.search([4,5,6,7,0,1,2],5))