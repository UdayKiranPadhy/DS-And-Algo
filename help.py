class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        N= len(nums)
        def LIS(index,curr,length):
            if index == N:
                return length
            
            if nums[index] > curr:
                return max(LIS(index+1,nums[index],length+1) , LIS(index+1,curr,length))
            else:
                return LIS(index+1,curr,length)
        
        return LIS(0,-10**4-1,0)