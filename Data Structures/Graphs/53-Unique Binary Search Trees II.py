"""

95. Unique Binary Search Trees II
Medium

4562

296

Add to List

Share
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8


"""

# Solution
"""

Let dfs(left, right) return all valid BSTs where values in the BST in range [left..right].
Then dfs(1, n) is our result.
To solve dfs(left, right), we just
Generate root value in range [left...right]
Get left subtrees by leftNodes = dfs(left, root-1)
Get right subtrees by rightNodes = dfs(root+1, right).
Add all combination between leftNodes and rightNodes to form root trees.
Can we cache the result of dfs(left, right) to prevent it to re-compute multiple time.
There is a simillar problem, which is 894. All Possible Full Binary Trees, try to solve it yourself.


"""


# https://leetcode.com/problems/unique-binary-search-trees/discuss/1565543/C%2B%2BPython-5-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Catalan-O(N)

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            ans = []
            for root in range(left, right+1):
                leftNodes = dfs(left, root - 1)
                rightNodes = dfs(root+1, right)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        ans.append(rootNode)
            return ans

        return dfs(1, n)
