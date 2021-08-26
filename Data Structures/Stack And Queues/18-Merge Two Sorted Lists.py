"""

21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""

# What we need to do in this problem is implement merge of two sorted list, such 
# that final list is also sorted: this is classical step for example for 
# well-known merge sort. To make our code more clean, we use dummy variable. 
# Then we have main steps in our algorithm:

# 1)Compare values in l1 and l2 nodes of our lists: if first one is smaller, attach it 
# to the end of new list and move it, if second one is smaller, do the same with it.
# 
# 2)We use condition while l1 and l2, that is if one of the lists finished, we still 
# have some ending of another list, which we need to attach to the end.
# 
# 3)Finally, just return node next to dummy variable in our list.
# 
# Complexity: time complexity is O(n+m), where n and m are lengths of our 
# lists: we traverse them only once. Space complexity is O(1), because we do not 
# create new objects and just reconnect already existing ones.

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = tail = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        return head.next