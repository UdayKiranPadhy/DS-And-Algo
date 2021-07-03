"""
        1                15  
       / \              /  \
      2   3    =>      11   3
     / \              /  \
    4   5            4    5

"""


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


def SumReplacement(root):
    if root == None:
        return 0
    l = SumReplacement(root.left)
    r = SumReplacement(root.right)
    root.val = root.val + l + r
    return root.val


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(SumReplacement(root))


if __name__ == '__main__':
    main()
