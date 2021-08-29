"""

25. Reverse Nodes in k-Group
Hard

4762

438

Add to List

Share
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
 

Follow-up: Can you solve the problem in O(1) extra memory space?

"""

# Problem statement
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Solution
# This is quite classical linked list problem and it is quite nasty in my opinion. 
# It can be a bit problematic to imagine all this in your head, do it on paper. 
# The idea is to add dummy variable, then calculate number of nodes. 
# We need this, because we do not need to reverse last group. 
# Then we use idea similar to problem 0206 Reverse Linked List: but here we 
# need to reverse k elements, and then reconnect first and last nodes in each 
# group and update cnt.

# Complexity
# Time complexity is O(n), space complexity is O(1).

# Code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        cur, nxt, pre = dummy, dummy, dummy
        cnt = 0
        while cur.next:
            cnt += 1
            cur = cur.next
            
        while cnt >= k:
            cur = new = pre.next
            nxt = cur.next
            for _ in range(k-1):
                tmp = nxt.next
                nxt.next = cur
                cur = nxt
                nxt = tmp
            
            pre.next = cur
            new.next = nxt
            pre = new
            cnt -= k
            
        return dummy.next