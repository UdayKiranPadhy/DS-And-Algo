class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:

        maxi = -1

        def LIS(m, n, nums1, nums2, curr):
            nonlocal maxi

            if m == len(nums1) or n == len(nums2):
                return
            if maxi < curr:
                maxi = curr
            if nums1[m] == nums2[n]:
                LIS(m+1, n+1, nums1, nums2, curr+1)
                LIS(m+1, n, nums1, nums2, 0)
                LIS(m, n+1, nums1, nums2, 0)
            else:
                LIS(m+1, n, nums1, nums2, 0)
                LIS(m, n+1, nums1, nums2, 0)
        LIS(0, 0, nums1, nums2, 0)
        return maxi


model = Solution()
print(model.findLength([70, 39, 25, 40, 7], [52, 20, 67, 5, 31]))
