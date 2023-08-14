class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def convert(root):
    if root is None:
        return 

    convert(root.left)
    convert(root.right)

    if not root.left:
        root.left = root.right
        root.right = None

    else:
        root.left.right = root.right
        root.right = None

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    convert(root)
    preorder(root)