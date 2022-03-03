# Definition for singly-linked list.
from math import ceil
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head

        # Calculate the length of LList
        length = 0
        while curr:
            length += 1
            curr = curr.next

        output = []
        prev = None
        curr = head
        while length:
            n = ceil(length/k) if length % k != 0 else k
            output.append(curr)
            length -= n
            while n:
                prev = curr
                curr = curr.next
                n -= 1
            prev.next = None
        while len(output) < k:
            output.append(None)
        return output


model = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(10)
print(model.splitListToParts(head, 5))
