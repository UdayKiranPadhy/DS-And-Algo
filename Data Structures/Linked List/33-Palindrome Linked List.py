"""

234. Palindrome Linked List
Easy

https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

"""

# (By reversing the list) 
# This method takes O(n) time and O(1) extra space. 
# 1) Get the middle of the linked list. 
# 2) Reverse the second half of the linked list. 
# 3) Check if the first half and second half are identical. 
# 4) Construct the original linked list by reversing the second half again and attaching
# it back to the first half


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        # reverse linked list now
        prev = None
        curr = slow

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        
        # Check for palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
