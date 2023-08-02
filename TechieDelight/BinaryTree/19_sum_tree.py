import sys

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isSumTree(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.key

    left = isSumTree(root.left)
    right = isSumTree(root.right)

    if left != -sys.maxsize and right != -sys.maxsize and root.key == left + right:
        return 2 * root.key

    return -sys.maxsize

if __name__ == "__main__":
    root = Node(44)
    root.left = Node(9)
    root.right = Node(13)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isSumTree(root) != -sys.maxsize:
        print("Binary tree is a sum tree")
    else:
        print("Binary tree is not a sum tree")