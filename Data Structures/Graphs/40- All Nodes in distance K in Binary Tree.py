"""

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

863. All Nodes Distance K in Binary Tree
Medium

Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) 
have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

"""

from collections import defaultdict
from statistics import mode
from tkinter.tix import Tree
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(node,parent):
            if node == None:
                return
            if parent != None:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        ans = []
        
        def dfs2(node,parent,level):
            if level == 0:
                ans.append(node)
                return
            for neibour in graph[node]:
                if neibour == parent:
                    continue
                dfs2(neibour,node,level-1)
        dfs2(target.val,None,k)
        return ans

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

model = Solution()
model.distanceK(root , root.left)