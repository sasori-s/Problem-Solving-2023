import sys

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printPath(root, total):
    if root is None and total == 0:
        return True

    if root is None:
        return False

    left = printPath(root.left, total - root.data)
    
    right = False
    if not left:
        right = printPath(root.right, total - root.data)

    if left or right:
        print(root.data, end=" ")

    return left or right

def rootToLeafSum(root):
    if root is None:
        return -sys.maxsize

    if root.left is None and root.right is None:
        return root.data

    left = rootToLeafSum(root.left)
    right = rootToLeafSum(root.right)

    return (left if left > right else right) + root.data

def findMaxSumPath(root):
    total = rootToLeafSum(root)
    print("The maximum sum is ", total)
    print("The maximum sum path is ", end=" ")

    printPath(root, total)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(10)
    root.right.left.left = Node(7)
    root.right.left.right = Node(9)
    root.right.right.right = Node(5)
 
    findMaxSumPath(root)