class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def transfrom(root):
    if root is None:
        return 0

    left = transfrom(root.left)
    right = transfrom(root.right)

    old = root.data
    root.data = left + right

    return root.data + old

if __name__ == "__main__":
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    transfrom(root)
    preorder(root)