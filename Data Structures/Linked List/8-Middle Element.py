# Find the middle of a given linked list

"""
Method 1: 
Traverse the whole linked list and count the no. of nodes. 
Now traverse the list again till count/2 and return the node at count/2. 

Method 2: 
Traverse linked list using two pointers. 
Move one pointer by one and the other pointers by two. 
When the fast pointer reaches the end slow pointer will reach the 
middle of the linked list.
"""


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
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()
main_point = llist.head
ref_point = llist.head

while ref_point.next:
    main_point = main_point.next
    ref_point = ref_point.next.next

print(main_point.data)