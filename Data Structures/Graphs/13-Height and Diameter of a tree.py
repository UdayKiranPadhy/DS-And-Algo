
class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


def Height(root):
    if root == None:
        return 0
    else:
        return max(Height(root.left), Height(root.right)) + 1


def diameter(root):
    if root == None:
        return 0
    left = Height(root.left)
    right = Height(root.right)
    op1 = left + right + 1
    op2 = diameter(root.left)
    op3 = diameter(root.right)
    return max(op1, op2, op3)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(Height(root))
    print(diameter(root))


if __name__ == '__main__':
    main()
