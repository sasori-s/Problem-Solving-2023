import sys

class Node:
    def __init__(self, data =None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root

def swap(root):
    left = root.left
    root.left = root.right
    root.right = left

def isBST(root, min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)

def checkForBST(root):
    if isBST(root, -sys.maxsize, sys.maxsize):
        print("The given Binary tree is BST")

    else:
        print("The given binary tree is not a BST")

if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)

    # swap(root)
    checkForBST(root)