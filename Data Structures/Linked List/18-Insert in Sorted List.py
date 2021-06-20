"""
Insert in a Sorted List 
Given a sorted singly linked list and a data, your task is to insert the data in the 
linked list in a sorted way i.e. order of the list doesn't change.

Example 1:
Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 19 25 36 47 58 69 80

Example 2:
Input:
LinkedList: 50->100
data: 75
Output: 50 75 100

Your Task:
The task is to complete the function sortedInsert() which should insert the 
element in sorted Linked List and return the head of the linked list

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 10^4
-99999 <= A[i] <= 99999, for each valid i
"""
def sortedInsert(head1, val):
    done=0
    new_node = Node(val)
    if head1.data >= val:
        new_node.next = head1
        return new_node
    prev = head1
    to_return = head1
    while head1:
        if head1.data >= val:
            done = 1
            prev.next = new_node
            new_node.next = head1
            break
        prev = head1
        head1 = head1.next
    if done == 0:
        prev.next = new_node
    return to_return