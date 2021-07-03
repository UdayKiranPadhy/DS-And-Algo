"""
        1      
       / \     
      2   3    => 1 3 5
     / \          
    4   5         

Return The Right View Of A Binary Tree
"""


from typing import Deque


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


def RightView(root):
    stack = Deque()
    right = []
    stack.append(root)
    while len(stack) > 0:
        N = len(stack)
        ggg = True
        for i in range(N):
            if ggg:
                right.append(stack[-1].val)
                ggg = False
            poped_element = stack.popleft()
            if poped_element.left != None:
                stack.append(poped_element.left)
            if poped_element.right != None:
                stack.append(poped_element.right)
    return right


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(*RightView(root))


if __name__ == '__main__':
    main()
