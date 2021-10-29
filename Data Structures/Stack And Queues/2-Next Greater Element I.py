"""

496. Next Greater Element I
Easy

1049

79

Add to List

Share
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

"""

# My Trail
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        N = len(nums2)

        for i in range(N-1, -1, -1):
            if len(stack) == 0:
                stack.append(nums2[i])
                res.append(-1)
            elif nums2[i] >= stack[-1]:
                while stack and nums2[i] >= stack[-1]:
                    stack.pop()
                if len(stack) == 0:
                    res.append(-1)
                    stack.append(nums2[i])
                else:
                    res.append(stack[-1])
                    stack.append(nums2[i])
            else:
                res.append(stack[-1])
                stack.append(nums2[i])
        print(res)
        lookup = {}
        for index, value in enumerate(res[::-1]):
            lookup[nums2[index]] = value

        ans = []
        for q in nums1:
            ans.append(lookup[q])
        return ans


# Problem statement
# https://leetcode.com/problems/next-greater-element-i/

# Solution
# Sizes of both arrays are small enough, so we just can do brute-force solution in
# O(m * n), where n is size of nums2 and m is size of nums1.

# If we want to solve this problem in O(n) time, it is not so simple. The idea is to
# traverse nums2 and keep stack with decreasing order of elements. When we try to add
# element, if it is less than last element of stack, we just add it. If it is more
# than the last element, we extract it from stack and also put it inside dic: correspondence
# between numbers and its next greater element: we need it, because we have also nums1,
# which we need to traverse after. Next, when we traverse nums1 we can use function .get(num, -1),
# which will return answer for num if it is inside dictionary and -1 if it was not found.

# Complexity
# Time and space complexity is O(n).

# Code
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []

        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            stack.append(num)

        return [dic.get(num, -1) for num in nums1]
