"""
Reorder List 

Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.

Example 1:
Input:
LinkedList: 1->2->3
Output: 1 3 2

Example 2:
Input:
LinkedList: 1->7->3->4
Output: 1 4 7 3.

Your Task:
The task is to complete the function reorderList() which should reorder the list as 
required. The reorder list is automatically printed by the driver's code.

Note: Try to solve without using any auxilliary space.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10^4
"""

def reorderList(head):
    arr = []
    while head:
        arr.append(head)
        head = head.next
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
    else:
        mid = len(arr) // 2 + 1
    left, right = arr[:mid], arr[mid:]
    right = right[::-1]
    arr[::2] = left
    arr[1::2] = right
    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]
    arr[len(arr)-1].next = None
    return arr[0]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    

def printlist(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("Null")

llist = LinkedList()
llist.push(10)
llist.push(80)
llist.push(70)
llist.push(60)
llist.push(50)
printlist(llist.head)
printlist(reorderList(llist.head))

