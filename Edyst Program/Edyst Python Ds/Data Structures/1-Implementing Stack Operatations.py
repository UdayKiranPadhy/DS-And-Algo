"""
Write a program to implement the following operations in a Stack:

Operations:

push:       To add the elements into Stack
pop:         To remove the element from Stack and return the element.
peek:        To get the top element from the Stack and return the element.
isEmpty:   returns 1 is stack is empty. Else returns 0
isFull:       returns 1 is stack is full. Else returns 0
Some code has already been written. Please use the given structure / class to write your own functions
"""


class Stack:
    def __init__(self, size):
        self.data = []
        self.size = size
        self.top = -1

    def push(self, val):
        self.data.append(val)
        self.top += 1
        return self.data

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def isFull(self):
        if len(self.data) == self.size:
            return 1
        else:
            return 0