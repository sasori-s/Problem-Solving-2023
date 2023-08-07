class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printNodes(root, diagonal, d):
    if root is None:
        return

    d.setdefault(diagonal, []).append(root.data)

    printNodes(root.left, diagonal + 1, d)
    printNodes(root.right, diagonal , d)


def printDiagonalNodes(root):
    d = {}
    printNodes(root, 0, d)

    for key in sorted(d.keys()):
        print(d.get(key))

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printDiagonalNodes(root)