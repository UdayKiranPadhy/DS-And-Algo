class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


# Start with the empty list
llist = LinkedList()

llist.head = Node(1)
second_node = Node(2)
third_node = Node(3)
""" 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    """

llist.head.next = second_node  # Link first node with second
""" 
    Now next of first Node refers to second.  So they 
    both are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    """

second_node.next = third_node  # Link second node with the third node
""" 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
"""


# Main part in linked list part is its traversels coz python internally makes
# User defined objects mutable so while removing a node careful during the traversal and pointing
# poinintg variable , u would only know the problem when u give that a try
