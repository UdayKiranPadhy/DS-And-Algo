"""
Given a linked list, delete N nodes after skipping M nodes of a linked list until 
the last of the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line 
of input contains number of elements in the linked list and next M and N respectively 
space separated. The last line contains the elements of the linked list.

Output:
Function should not print any output to stdin/console.

User Task:
The task is to complete the function linkdelete() which should modify the linked list 
as required.

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output: 
9 1 5 9 10 1
1 2 3 4 5 6

Explanation:
Testcase 1: Deleting one node after skipping the M nodes each time, 
we have list as 9-> 1-> 5-> 9-> 10-> 1.
"""


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = self.head
        newnode = Node(int(value))
        self.head=newnode
        newnode.next = temp
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end="-> ")
            temp = temp.next
        print()

def skipMdeleteN(head, M, N):
    while(head): 
        for count in range(1, M): 
            if head is None: 
                return 
            head = head.next 
        if head is None : 
            break
        t = head.next
        for count in range(1, N+1): 
            if t is None: 
                break
            t = t.next
        head.next = t 
        head = t 

llist = LinkedList()
llist.push(10)
llist.push(15)
llist.push(5)
llist.push(50)
llist.push(60)
llist.push(40)
llist.push(30)
llist.push(10)
llist.push(70)
llist.printlist()
skipMdeleteN(llist.head, 2, 1)
llist.printlist()