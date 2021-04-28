"""

InfyTQ - merge K sorted lists
Merge k sorted linked lists and return it as one sorted list.

Input:

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
Output :

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
Input :

    3 -> 3 -> 4 -> 4
    1 -> 1 -> 3 -> 4 -> 5
Output :

    1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5

"""
class Solution:
    arr = []

    def __init__(self):
        self.arr = []

    def mergeKLists(self, A):
        for i in A:
            if i == None:
                continue
            while i.next != None:
                self.arr.append(i.val)
                i = i.next
            self.arr.append(i.val)
        self.arr.sort()
        for i in self.arr:
            print(i, end=" ")
