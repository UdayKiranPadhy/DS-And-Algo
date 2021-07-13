"""
Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""


# Solution
"""
Solution
What we need to do in this problem is to perform usual schoolbook addition. Our linked lists already given in reverse order, and as in usual addition we need to start from the end. We continue to add until we still have digits to traverse. Imagine, that we need to add two numbers 986 and 47.

add 6 and 7, so we have digit 3 and carry equal to 1.
add 8 and 4 and 1, so we have 3 and carry equal to 1.
add 9 from first number, and we do not have anything from second, so we choose 0 from second. Also we have curry equal to 1, finally we have digit 0 and carry equal to 1.
We still have carry, but no digits left, so we evaluate 0+0+1=1. And now we can stop, we do not have digits and we do not have carry.
Final number we constructed is 1033.
Complexity
Time complexity is O(m+n), where m and n are lengths of our linked lists, space complexity is O(max(m,n)) if we count answer as memory or O(1) if we do not.

"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = curr = ListNode(0)

        while l1 or l2 or carry:
            d1, d2 = 0, 0
            if l1:
                d1 = l1.val
                l1 = l1.next
            if l2:
                d2 = l2.val
                l2 = l2.next
            carry, digit = divmod(d1 + d2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return head.next
