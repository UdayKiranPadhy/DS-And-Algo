"""

662. Maximum Width of Binary Tree
Medium

4106

648

Add to List

Share
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
Accepted
166,301
Submissions
415,302

"""


# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        INF = float('inf')
        leftmost = defaultdict(lambda: INF)
        rightmost = defaultdict(lambda: -INF)

        def go(node, level, index):
            if node == None:
                return
            leftmost[level] = min(leftmost[level], index)
            rightmost[level] = max(rightmost[level], index)

            go(node.left, level + 1, 2*index + 1)
            go(node.right, level + 1, 2 * index + 2)
        answer = -1
        for i in leftmost.keys():
            answer = max(answer, rightmost[i] - leftmost[i])
        return answer
