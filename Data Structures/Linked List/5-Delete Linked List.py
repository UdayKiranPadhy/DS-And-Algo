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
        while count < position - 1 and temp:
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

    def deleteNode(self, position):
        # If linked list is empty
        if self.head == None:
            return
        # Store head node
        temp = self.head
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
        # Unlink the node from linked list
        temp.next = None
        temp.next = next
    
    def deletelist(self):
        current = self.head

        while current:
            prev = current.next
            del current
            current = prev




    def deletelist2(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
# Not able to delete linked list

# I want to delete a LinkedList , memory also del

llist = LinkedList()
llist.push(10)
llist.push(9)
llist.push(7)
llist.push(5)
llist.push(6)
llist.push(4)
llist.push(3)
llist.printlist()
llist.deletelist2()
llist.printlist()