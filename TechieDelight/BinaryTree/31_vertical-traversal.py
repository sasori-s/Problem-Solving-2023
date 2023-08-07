from collections import defaultdict

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printVertical(node, dist, d):
    if node is None:
        return 
    
    d.setdefault(dist, []).append(node.data)

    printVertical(node.left, dist - 1, d)
    printVertical(node.right, dist + 1, d)



def printVerticalTree(root):
    if root is None:
        return None

    d = {}
    printVertical(root, 0, d)

    for value in d.values():
        print(value)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)

    printVerticalTree(root)