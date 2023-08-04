from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isLeaf(node):
    return node.left is None and node.right is None

def printPaths(node, path):
    if node is None:
        return
    
    path.append(node.data)

    if isLeaf(node):
        print(list(path))

    printPaths(node.left, path)
    printPaths(node.right, path)

    path.pop()

def printRootToLeafPath(root):
    path = deque()
    printPaths(root, path)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)

    printRootToLeafPath(root)