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


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()

"""
Method-1
Using Stack Operations 
A simple solution is to use a stack of list nodes. This mainly involves three steps.
Traverse the given list from head to tail and push every visited node to stack.
Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
If all nodes matched, then return true, else false.
"""

# point = llist.head
# l=[]
# while point:
#     l.append(point.data)
#     point = point.next
# point = llist.head
# while point:
#     temp = l.pop()
#     if point.data == temp:
#         point = point.next
#     else:
#         print("Not a palindrome")
#         break
# print("Palindrome")

"""
Method-2
Double pointer
Place one start other at the end and keep moving 
"""

"""
METHOD 2 (By reversing the list) 
This method takes O(n) time and O(1) extra space. 
1) Get the middle of the linked list. 
2) Reverse the second half of the linked list. 
3) Check if the first half and second half are identical. 
4) Construct the original linked list by reversing the second half again and attaching
it back to the first half
"""