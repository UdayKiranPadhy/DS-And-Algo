"""
Remove every k'th node 
Given a singly linked list, your task is to remove every kth node from the linked list.

Input:
The first line of input contains number of test cases T. Then T test cases follow. 
Every test case contains 3 lines. First line of every test case contains an integer 
N denoting the size of the linked list . The second line contains N space separated 
values of the linked list. The third line contains an integer K.

Output:
Output for each test case will be space separated values of the nodes of the new 
transformed linked list.

User Task:
The task is to complete the function deleteK() which should delete every kth nodes 
from the linked list.

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= element of linked list <= 1000
0 <= k <= 100

Example:
Input:
2
8
1 2 3 4 5 6 7 8
3
4
1 2 3 4
2

Output:
1 2 4 5 7 8
1 3

Explanation:
Testcase 1: After removing every 3rd element from the linked list, 
we have updated list as 1, 2, 4, 5, 7 and 8, and the elements 
which are removed are 3 and 6.
"""
# Your task is to complete this function
# Your function should return the new head pointer
# def deleteK(head, k):
#     # 1 2 3 4 5 6 7 8
#     if k == 1:
#         return None

#     while (head):
#         for i in range(1, k - 1):
#             if head:
#                 head = head.next
#         if head == None:
#             return head
#         t = head.next
#         if t.next:
#             head.next = t.next
#             head = t
#     return head

"""
Did not work , says time limit exceeded
"""


def deleteK(head, k):
    if k == 1:
        return None
    count = 1
    curr = head
    while head:
        if count == k - 1 and head.next:
            head.next = head.next.next
            count = 0
            continue
        head = head.next
        count += 1
    return curr


"""
That code gives correct answer but Geeks and geeks tells it run time run and dont know where
"""


def deleteK2(head, k):

    # If linked list is empty
    if head == None:
        return None

    if k == 1:
        return None

    # Initialize ptr and prev before
    # starting traversal.
    ptr = head
    prev = None

    # Traverse list and delete every k-th node
    count = 0
    while ptr != None:

        # increment Node count
        count = count + 1

        # check if count is equal to k
        # if yes, then delete current Node
        if k == count:

            # put the next of current Node in
            # the next of previous Node
            # delete(prev.next)
            prev.next = ptr.next

            # set count = 0 to reach further
            # k-th Node
            count = 0

        # update prev if count is not 0
        if count != 0:
            prev = ptr

        ptr = prev.next

    return head


"""
Deletek2 is the answer.
"""

# Driver Code
class node:
    def __init__(self):
        self.data = None
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = int(input())
        for i in values:
            llist.insert(i)
        head = deleteK(llist.get_head(), k)
        printlist(head)
        print("")
