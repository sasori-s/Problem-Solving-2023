import  sys

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBST(root, minKey, maxKey):
    if root is None:
        return True

    if root.data < minKey and root.data > maxKey:
        return False

    return isBST(root.left, minKey, root.data) and\
        isBST(root.right, root.data, maxKey)


def checkBST(root):
    if isBST(root, -sys.maxsize, sys.maxsize):
        print('The tree is BST')
    else:
        print("The tree is not a BST")


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]
    root = None

    for key in keys:
        root = insert(root, key)

    # swap(root)
    checkBST(root)