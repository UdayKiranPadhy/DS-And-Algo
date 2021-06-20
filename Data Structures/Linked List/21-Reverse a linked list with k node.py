"""
Reverse a Linked List in groups of given size. 
Medium Accuracy: 45.83% Submissions: 69757 Points: 4
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4
Your Task:
The task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)
"""


def reverse(head,k):
    prev = None
    curr = head
    count=0
    while (curr) and count <k:
        next = curr.next
        curr.next = prev
        prev= curr
        curr = next
        count+=1

    if curr:
        head.next = reverse(curr,k)

    return prev
    
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
        k = int(input())
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        head = reverse(lis.head,k)
        printList(head)