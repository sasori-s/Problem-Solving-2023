class Node:
    def __init__(self, data=None, left=None, right=None) :
        self.data = data
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def swap(root):
    if root is None:
        return 

    temp = root.left
    root.left = root.right
    root.right = temp


def convertToMirror(root):
    if root is None:
        return

    convertToMirror(root.left)
    convertToMirror(root.right)

    swap(root)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    convertToMirror(root)
    preorder(root)