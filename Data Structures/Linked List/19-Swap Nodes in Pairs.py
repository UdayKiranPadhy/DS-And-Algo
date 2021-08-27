"""

24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's 
nodes (i.e., only nodes themselves may be changed.)
 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""

# Problem Link :- https://leetcode.com/problems/swap-nodes-in-pairs/

# Solution
# As with a lot of other linked lists, it is good idea to add dummy node before
# list to avoid cases. Imagine, we have list 1, 2, 3, 4, 5, 6, let us add 0 node
# in the beginning, so we have 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 now.

# Now, let us look at the main step of algorithm (for simplicity I will call nodes by its values)

# pre = 0, whe check if pre.next and pre.next.next exists, they are, so define a = 1 and b = 2.
# Now, we need to rewrite links: 0 -> 2, 2 -> 1 and 1 -> 3. Note, that we do it all in one step.
# Finally, we say, that pre = 1. Also, our list now looks like 0 -> 2 -> 1 -> 3 -> 4 -> 5 -> 6 and
# as I said pre = 1 now, so we swapped first two elements and now we on element number 2, which is
# exaclty what we have previously for smaller list.
# On next step we have 0 -> 2 -> 1 -> 4 -> 3 -> 5 -> 6 and finally 0 -> 2 -> 1 -> 4 -> 3 -> 6 -> 5,
# this is exaclty what we need to return.

# Complexity
# Time complexity is O(n): we iterate over our list once, space complexity is O(1):
# we did not add any new space and reused already existing nodes.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = a.next
            dummy.next, a.next, b.next = b, b.next, a
            dummy = a
        return pre.next
