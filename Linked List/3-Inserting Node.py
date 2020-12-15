class Node():
    """
    Creates a Node , Parameters are value.
    """
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    """
    Creats a linked list Object , Parametets None
    Functions PrintList
    Variables Head
    """
    def __init__(self):
        self.head = None
        
    def printlist(self):
        print(" Linked list Looks like : ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

#Initilize a LinkedList
llist = LinkedList()

# Initilize Nodes for Linked List
first = Node(10)
second = Node(15)
third = Node(20)
fourth = Node(25)

# Connect everything
llist.head = first
first.next = second
second.next = third
third.next = fourth

llist.printlist()

"""
Inserting of a node can take place at 3 ways:
1)Insertion at head
2)Insertion at middle
3)Insertion at the end
"""

#Insertion at head

insert_node = Node(5)
#Store the head node
temp = llist.head
#Change the head node
llist.head = insert_node
#Connect the next the older head
insert_node.next = temp
llist.printlist()

# Insertion at middle
insert_node = Node(22)
# We will insert it in middle of 20 and 25
temp = llist.head
while (temp.data != 20 and temp):
    temp = temp.next

insert_node.next = temp.next
temp.next = insert_node

llist.printlist()


