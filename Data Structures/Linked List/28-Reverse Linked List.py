"""

206. Reverse Linked List
Easy

10767

184

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nex = None

        while curr and curr.next:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        if curr:
            curr.next = prev
        return curr


# Recursive Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        self.new_head = None

        def reverse(node, parent):
            if node.next == None:
                self.new_head = node
                node.next = parent
                return
            reverse(node.next, node)
            node.next = parent
        reverse(head, None)
        return self.new_head
