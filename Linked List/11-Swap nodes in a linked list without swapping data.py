# Swap nodes in a linked list without swapping data
"""
Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links. Swapping data of nodes may be expensive in many situations when data contains many fields. 
It may be assumed that all keys in the linked list are distinct.
Examples: 

Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Input:  10->15->12->13->20->14,  x = 10, y = 20
Output: 20->15->12->13->10->14

Input:  10->15->12->13->20->14,  x = 12, y = 13
Output: 10->15->13->12->20->14
"""

class Node():
    def __init__(self, value):
        self.data = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    def push(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

llist = LinkedList()
llist.push(50)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(10)

"""
Now swap 40 and 20
"""
X = 40
Y= 20

temp = self.head
while temp:
    if temp.next.data == X:
        prevX = temp
        currX = temp.next
    if temp.next.data == Y:
        prevY = temp
        currY = temp.next

temp = prevX
prevX.next = currY
currY.next