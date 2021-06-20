# Problem is to detect a loop in Linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList(object):
    """
    docstring
    """

    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        print(" Linked list Looks like : ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

llist = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fouth = Node(4)
fiveth = Node(5)

llist.head = first
first.next = second
second.next = third
third.next = fouth
fouth.next = fiveth
fiveth.next = second

"""
Method - 1
Hashing method , in python try set and keep the id of node if there is already a id in set return True
Loop detected
"""

temp = llist.head
A = set()
while temp:
    if id(temp) in A:
        print("Loop detected")
        break
    A.add(id(temp))
    temp = temp.next

"""
Method-2
Modifing the Node Class and adding a flag variable
"""

