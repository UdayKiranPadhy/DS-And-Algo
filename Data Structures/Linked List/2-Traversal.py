class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        tempnode = self.head
        while tempnode:
            print(tempnode.data)
            tempnode = tempnode.next


llist = LinkedList()

first_node = Node(5)
second_node = Node(10)
third_node = Node(15)

llist.head = first_node
first_node.next = second_node
second_node.next = third_node

llist.printlist()
