class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def printRightToLeft(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.data, end=" ")
        return True

    right = printRightToLeft(root.right, level - 1)
    left = printRightToLeft(root.left, level - 1)

    return left or right


def printLeftToRight(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.data, end=" ")
        return True

    left = printLeftToRight(root.left, level - 1)
    right = printLeftToRight(root.right, level - 1)

    return left or right


def spiralOrderTraversal(root):
    if root is None:
        return 
    
    level = 1
    process = True

    while process:
        process = printLeftToRight(root, level)
        level += 1

        if process:
            process = printRightToLeft(root, level)
            level += 1


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    
    spiralOrderTraversal(root)