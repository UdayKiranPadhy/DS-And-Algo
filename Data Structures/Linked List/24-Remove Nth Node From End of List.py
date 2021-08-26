"""

19. Remove Nth Node From End of List
Medium

6500

349

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

"""

# Problem statement
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Solution
# Two passes solution is straightforward. For one pass solution we use the
# idea of 2 iterators, let one of them start at the beginning, another at index n,
# then when the second one is finished, the first one will be on the right place.

# Complexity
# Time complexity is O(L), more precisely we make 2L-n steps, where L is length of
# list, space complexity is O(1). So it the end it is exactly the same as staightforward
# two passes solution. So, if you meet this problem in real interview, you can just
# explain two pass solution, and when interviewer say can you do better: explain
# him that another one pass solution in fact is exaclty the same time and space.

# Code

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        P1, P2 = dummy, dummy
        for _ in range(n):
            P2 = P2.next

        while P2.next:
            P1 = P1.next
            P2 = P2.next

        P1.next = P1.next.next

        return dummy.next
