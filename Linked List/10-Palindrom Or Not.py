# Function to check if a singly linked list is palindrome

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

"""
Method-1
Using Stack Operations 
A simple solution is to use a stack of list nodes. This mainly involves three steps.
Traverse the given list from head to tail and push every visited node to stack.
Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
If all nodes matched, then return true, else false.
"""
