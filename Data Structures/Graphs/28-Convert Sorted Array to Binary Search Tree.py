"""

108. Convert Sorted Array to Binary Search Tree
Easy

4953

312

Add to List

Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

"""

from typing import List, Optional


# Space: O(log n): Excluding the result array(not being considered as auxiliary in space complexity analysis), only need to store the height of the balanced tree, which is log n given n is the number of elements of the input array.
# Time: O(n): One pass each element to form nodes.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if left > right:
                return None

            p = (left + right) // 2
            if (left + right) % 2:
                p += 1

            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p + 1, right)

            return root

        return helper(0, len(nums) - 1)
