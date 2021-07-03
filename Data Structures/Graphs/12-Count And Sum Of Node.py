"""
Date :- 30/6/21
Source Youtube

Count all the nide in a binary tree .

"""


def count(root):
    if root == None:
        return 0
    else:
        return count(root.left) + count(root.right) + 1


def Sum(root):
    if root == None:
        return 0
    else:
        return root.val + Sum(root.left) + Sum(root.right)


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(count(root))
    print(Sum(root))


if __name__ == '__main__':
    main()
