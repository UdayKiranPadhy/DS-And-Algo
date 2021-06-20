"""
https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
1879. Minimum XOR Sum of Two Arrays
Hard

You are given two integer arrays nums1 and nums2 of length n.

The XOR sum of the two integer arrays is 
(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) 
(0-indexed).

For example, the XOR sum of [1,2,3] and [3,2,1] is equal to 
(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

Return the XOR sum after the rearrangement. 

Example 1:

Input: nums1 = [1,2], nums2 = [2,3]
Output: 2
Explanation: Rearrange nums2 so that it becomes [3,2].
The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.


Example 2:

Input: nums1 = [1,0,3], nums2 = [5,3,4]
Output: 8
Explanation: Rearrange nums2 so that it becomes [5,4,3]. 
The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.
 

Constraints:

n == nums1.length
n == nums2.length
1 <= n <= 14
0 <= nums1[i], nums2[i] <= 107


"""
from functools import lru_cache


class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        N = len(nums1)

        @lru_cache(None)
        def XOR(i, mask):
            if i == N:
                return 0

            best = float('inf')
            for x in range(N):
                if (mask & (1 << x)) == 0:
                    best = min(best, (nums1[i] ^ nums2[x]) +
                               XOR(i+1, mask | (1 << x)))
            return best
        return XOR(0, 0)


model = Solution()
num1 = [int(x) for x in input().split(" ")]
num2 = [int(x) for x in input().split(" ")]
print(model.minimumXORSum(num1, num2))
