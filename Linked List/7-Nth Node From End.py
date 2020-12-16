# Program for n’th node from the end of a Linked List

"""
Method 1 (Use length of linked list) 
1) Calculate the length of Linked List. Let the length be len. 
2) Print the (len – n + 1)th node from the beginning of the Linked List. 
Childs Play right ? Right !
"""

"""
Method 2 (Double Pointer)
Maintain two pointers – reference pointer and main pointer. 
Initialize both reference and main pointers to head. 
First, move the reference pointer to n nodes from head. 
Now move both pointers one by one until the reference pointer reaches the end. 
Now the main pointer will point to nth node from the end. Return the main pointer.
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
llist.push(10)
llist.push(9)
llist.push(7)
llist.push(5)
llist.push(6)
llist.push(4)
llist.push(3)

"""
Suppose We need to find the 3rd element from end, keep two pointer at head point
"""
llist.printlist()

main_point = llist.head
ref_point = llist.head

for i in range(3):
    ref_point = ref_point.next

while ref_point:
    main_point = main_point.next
    ref_point = ref_point.next

print(main_point.data)


"""
Need to try 
void printNthFromLast(struct Node* head, int n) 
{ 
    static int i = 0; 
    if (head == NULL) 
        return; 
    printNthFromLast(head->next, n); 
    if (++i == n) 
        printf("%d", head->data); 
} 
"""