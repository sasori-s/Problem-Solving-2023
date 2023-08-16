class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def printLeftViewUtil(root, d, level):
    if root is None:
        return

    if d.get(level) is None:
        # d.get(level).append(root.key)
        d[level] = root.key

    printLeftViewUtil(root.right, d, level + 1)
    printLeftViewUtil(root.left, d, level + 1)


def printLeftView(root):
    d = {}
    printLeftViewUtil(root, d, 0)
    
    for values in d.values():
        print(values, end=" ")

if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    printLeftView(root)
