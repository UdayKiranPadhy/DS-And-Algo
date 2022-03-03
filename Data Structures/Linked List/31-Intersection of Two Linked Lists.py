"""

160. Intersection of Two Linked Lists
Easy


Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

Image 1

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

"""


# We need two pointers: p1 starts from headA and p2 starts from headB.
# The key point is how we make sure the two pointers come to the intersection node at the same time.
# Since the difference of the distance to the intersection is the difference of the length of the two list. We can "link" the two list together:

# Let p1 starts from headA passing through the first linked list, then the second (starting from headB).
# Let p2 starts from headB passing through the second linked list, then the first (starting from headA).
# Thus, the number of steps they need to take to arrive the intersection node is equal.
# Also, if there is no intersection, it will end up with p1 == p1 == null.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1


# Assume there exists an intersection. The intersection is None if A and B don't actually intersect. Notice that the following equation is true:

# a + b + 2*c == m + n

# a = number of edges from headA to the intersection node
# b = number of edges from headB to the intersection node
# c = number of edges from the intersection node to the tail
# m = number of edges from headA to the tail
# n = number of edges from headB to the tail
# To find the intersection node, we want to solve for a or b. If we have a, then we can travel a distance of a away from headA and arrive at the intersection node. Alternatively, if we have b then we can travel a distance of b away from headB and arrive at the intersection node.

# Now, notice the following:

# a + (n - m) == b

# (assuming n > m)
# If m > n, then instead:

# b + (m - n) == a
# It's easy to prove. For example, for the n > m case:

# a + (n - m) == b
# (m - c) + (n - m) == (n - c)
# m - m + n - c == n - c
# n - c == n - c
# So we just need to find the value of n - m and then give the iterator at headB a head start of n - m. Conversely, if m > n, then we give the iterator at headA a head start of m - n. Then iterate both at the same speed, and eventually they will arrive at the intersection point at the same time.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate m
        m, a = 0, headA
        while a:
            m += 1
            a = a.next
        # Calculate n
        n, b = 0, headB
        while b:
            n += 1
            b = b.next

        # Restart a, b at headA, headB
        # Give either a or b a "head start"
        a, b = headA, headB
        if m > n:
            # Give 'a' a head start of (m - n)
            for _ in range(m - n):
                a = a.next
        else:
            # Give 'b' a head start of (n - m)
            for _ in range(n - m):
                b = b.next
        # Iterate a and b until the intersect.
        while a and b and a != b:
            a = a.next
            b = b.next
        return a
# Actually, we can make the code smaller like so:


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a = a.next
                b = b.next
        return a
