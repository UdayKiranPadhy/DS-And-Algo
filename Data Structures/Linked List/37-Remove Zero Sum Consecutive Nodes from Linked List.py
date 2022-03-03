"""

1171. Remove Zero Sum Consecutive Nodes from Linked List
Medium

1326

67

Add to List

Share
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.


"""


# Intuition
# Assume the input is an array.
# Do you know how to solve it?
# Scan from the left, and calculate the prefix sum.
# Whenever meet the seen prefix,
# remove all elements of the subarray between them.


# Solution 1
# Because the head ListNode can be removed in the end,
# I create a dummy ListNode and set it as a previous node of head.
# prefix calculates the prefix sum from the first node to the current cur node.

# Next step, we need an important hashmap m (no good name for it),
# It takes a prefix sum as key, and the related node as the value.

# Then we scan the linked list, accumulate the node's value as prefix sum.

# If it's a prefix that we've never seen, we set m[prefix] = cur.
# If we have seen this prefix, m[prefix] is the node we achieve this prefix sum.
# We want to skip all nodes between m[prefix] and cur.next (exclusive).
# So we simplely do m[prefix].next = cur.next.
# We keep doing these and it's done.


# Complexity
# Time O(N), one pass
# SpaceO(N), for hashmap


# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
