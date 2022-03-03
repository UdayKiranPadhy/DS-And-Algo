"""

328. Odd Even Linked List
Medium

4988

380

Add to List

Share
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = ListNode(0)
        head1 = odd
        even = ListNode(0)
        head2 = even
        curr = head
        oddi = True
        while curr:
            if oddi:
                odd.next = curr
                odd = odd.next
                curr = curr.next
                oddi = False
            else:
                even.next = curr
                even = even.next
                curr = curr.next
                oddi = True
        even.next = None
        odd.next = head2.next
        return head1.next
