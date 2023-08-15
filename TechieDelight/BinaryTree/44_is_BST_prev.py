import sys

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:
        insert(root.right, key)

    return root

def swap(root):
    left = root.left
    root.left = root.right
    root.right = left

def checkForBST(root):
    prev = Node(-sys.maxsize)

    if isBST(root, prev):
        print("The binary tree is a BST")
    else:
        print("The binary tree is not a BST")

def isBST(node, prev):
    if node is None:
        return True

    left = isBST(node.left, prev)

    if node.data <= prev.data:
        return False

    prev.data = node.data

    return left and isBST(node.right, prev)

    

if __name__ == "__main__":
    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    
    for key in keys:
        root = insert(root, key)

    swap(root)
    checkForBST(root)