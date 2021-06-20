"""
link :- https://leetcode.com/problems/binary-tree-maximum-path-sum/
Date : 20/6/2021 ,mrng 6:45

124. Binary Tree Maximum Path Sum
Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000



"""


# My trails 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        result = -sys.maxsize
        
        def dfs(root):
            nonlocal result
            if root==None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            
            op1 = max( max(l,r,0) + root.val , root.val )
            op2 = max( op1 , l + r + root.val,l,r )
            return op2
        
        return dfs(root)



# Original Answer

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = [float("-inf")]
        def search(node, curr_max):
            if not node:
                return 0
            left_max = search(node.left, curr_max)
            right_max = search(node.right,curr_max)

            single_max = max(0,left_max, right_max)+node.val # case1 and case 2
            double_max = max(single_max, left_max+right_max+node.val) # case 3

            ans[0] = max(ans[0], single_max, double_max)
            # remember to return the value of case 1 and case 2, since if we go up, current node can't be the "root" node
            return single_max 
        search(root, 0)
        return ans[0]