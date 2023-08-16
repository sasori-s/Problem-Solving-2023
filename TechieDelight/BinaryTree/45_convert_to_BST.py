class Node:
    def __init__(self, data=None, left=None, right=None ):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def extractKeys(root, keys):
    if root is None:
        return 

    extractKeys(root.left, keys)
    keys.append(root.data)
    extractKeys(root.right, keys)

def convertToBST(root, it):
    if root is None:
        return

    convertToBST(root.left, it)
    root.data = next(it)
    convertToBST(root.right, it)

def convert(root):
    keys = list()

    extractKeys(root, keys)
    it = iter(set(keys))
    convertToBST(root, it)

if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(10)
    root.left.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(6)

    convert(root)
    inorder(root)