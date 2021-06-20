"""
Pairwise swap elements of a linked list 

Given a singly linked list of size N. The task is to swap elements in 
the linked list pairwise.
For example, if the input list is 1 2 3 4, 
the resulting list after swaps will be 2 1 4 3.

Example 1:
Input:
LinkedList: 1->2->2->4->5->6->7->8
Output: 2 1 4 2 6 5 8 7
Explanation: After swapping each pair
considering (1,2), (2, 4), (5, 6).. so
on as pairs, we get 2, 1, 4, 2, 6, 5,
8, 7 as a new linked list.

Your Task:
The task is to complete the function pairWiseSwap() which takes the head 
node as the only argument and returns the modified head.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 10^3
"""

def pairWiseSwap(head):
    to_return = head
    curr =Node(0)
    while head:
        head = swap(head, head.next)
        head = head.next.next
    return to_return

def swap(first, second):
    first.next = second.next
    second.next = first
    return second

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(1):
        arr = [int(x) for x in input().split()]
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        head = pairWiseSwap(lis.head)
        printList(head)