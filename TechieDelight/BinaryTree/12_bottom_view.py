class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def printTop(root, dist, level, d):
    if root is None:
        return

    if dist not in d or d[dist][1] <= level:
        d[dist] = (root.key, level)

    printTop(root.left, dist - 1, level + 1, d)
    printTop(root.right, dist + 1, level + 1, d)

def printTopView(root):
    d = {}
    printTop(root, 0, 0, d)

    for key in sorted(d.keys()):
        print(d.get(key)[0], end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    printTopView(root)