class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def preorder(root, level, dict):
    if root is None:
        return

    dict[level] = dict.get(level, 0) + 1

    preorder(root.left, level + 1, dict)
    preorder(root.right, level + 1, dict)

def findWidth(root):
    if root is None:
        return

    dict = {}

    preorder(root, 1, dict)
    print("The maximum width is, ", max(dict.values()))

if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    findWidth(root)