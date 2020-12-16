# Node class  
class Node:
    """
    Creates a Node , Parameters are value = data in the node.
    """
    # Constructor to initialize the node object  
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    """
    Creats a linked list Object , Parametets None
    Functions PrintList
    Variables Head
    """
    # Function to initialize head  
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        """
        Function to insert a new node at the beginning
        """ 
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node

    def insert(self, value, position):
        new_node = Node(value)
        count = 0
        temp = self.head
        while count < position-1 and temp:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
            


    
    def printlist(self):
        print(" Linked list Looks like : ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()



llist = LinkedList()
llist.push(7)
llist.push(8)
llist.push(5)
llist.push(2)
llist.printlist()

#Deletion at middle
"""
Deleting at middle value 8
"""

temp = llist.head
while temp.data != 8:
    if temp.next.data == 8:
        break
    temp = temp.next

temp.next = temp.next.next

llist.printlist()

"""
Deleting At end
"""
temp = llist.head
if temp.next == None:
    llist.head = None
temp = llist.head
while temp.next.next:
    temp = temp.next
del temp.next
temp.next = None
llist.printlist()