class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isSibling(root, a, b):
    if root is None:
        return False

    if (root.left == a and root.right == b ) or (root.left == b and root.right == a)  or isSibling(root.left, a, b) or isSibling(root.right, a, b):
        return True
    
    else:
        return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(isSibling(root, root.right.left, root.right.right))