import sys

def isBST(root):
    return isBSTUtill(root, -sys.maxsize, sys.maxsize)

def isBSTUtill(root, min, max):
    if not root:
        return

    if root.data < min or root.data > max:
        return False

    return (isBSTUtill(root.left, min, root.data - 1) and isBSTUtill(root.right, root.data + 1, max))