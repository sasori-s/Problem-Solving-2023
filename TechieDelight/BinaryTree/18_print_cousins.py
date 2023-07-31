class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def findLevel(root, x, index=1, level=0):
    if root is None or level != 0:
        return level

    if root == x:
        level = index

    level = findLevel(root.left, x, index+1, level)
    level = findLevel(root.right, x, index+1, level)

    return level

def printLevel(root, node, level):
    if root is None:
        return
    
    if level == 1:
        print(root.key, end=" ")
        return
    
    if not(root.left is not None and root.left == node or
           root.right is not None and root.right == node):
           printLevel(root.left, node, level-1)
           printLevel(root.right, node, level-1)

def printAllCousins(root, node):
    if root is None or root == node:
        return
    
    level = findLevel(root, node)
    printLevel(root, node, level)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    printAllCousins(root, root.right.left)
