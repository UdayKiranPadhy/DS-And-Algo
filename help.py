# Definition for a binary tree node.
from collections import defaultdict
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        INF = float('inf')
        leftmost = defaultdict(INF)
        rightmost = defaultdict(-INF)

        def go(node,level,index):
            if node == None:
                return
            leftmost[level] = min(leftmost[level],index)
            rightmost[level] = max(rightmost[level],index)

            go(node.left,level + 1 , 2*index + 1)
            go(node.right , level + 1, 2 * index + 2)
        answer = -1
        for i in leftmost.keys():
            answer = max(answer,rightmost[i] - leftmost[i])
        return answer