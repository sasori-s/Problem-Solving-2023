class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isLeaf(node):
    return node.left is None and node.right is None

def truncate(root):
    if root is None:
        return None

    root.left = truncate(root.left)
    root.right = truncate(root.right)

    if (root.left and root.right ) or isLeaf(root):
        return root

    child = root.left if root.left else root.right
    return child

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    

if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.left = Node(4)
    root.left.left.left = Node(5)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)

    root = truncate(root)
    inorder(root)