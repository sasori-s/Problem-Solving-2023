import sys

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isPresent(root, node):
    if root is None:
        return False

    if root == node:
        return True

    return isPresent(root.left, node) or isPresent(root.right, node)

def findLCA(root, a, b):
    if root is None:
        return None

    if root == a or root == b:
        return root

    left = findLCA(root.left, a, b)
    right = findLCA(root.right, a, b)

    if left and right:
        return root

    if left:
        return left
    
    if right:
        return right
    
    return None

def findLevel(root, node, level):
    if root is None:
        return -sys.maxsize

    if root == node:
        return level

    left = findLevel(root.left, node, level + 1)

    if left != -sys.maxsize:
        return left
    
    return findLevel(root.right, node, level + 1)


def findDistance(root, a, b):
    if root is None:
        return -sys.maxsize

    lca = None

    if isPresent(root, a) and isPresent(root, b):
        lca = findLCA(root, a, b)

    else:
        return -sys.maxsize
    
    return findLevel(lca, a, 0) + findLevel(lca, b, 0)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.right.right = Node(8)

    print(findDistance(root, root.right.left.left, root.right.right))