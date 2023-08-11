class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return 

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def fullBinary(root):
    if root is None:
        return root

    if (not root.left and not root.right):
        return root

    if not root.left:
        child = fullBinary(root.right)
        return child

    if not root.right:
        child = fullBinary(root.left)
        return child

    root.left = fullBinary(root.left)
    root.right = fullBinary(root.right)

    return root

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.left = Node(4)
    root.left.left.left = Node(5)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)

    root = fullBinary(root)
    inorder(root)