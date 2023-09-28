class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class NodeInfo:
    def __init__(self, node = None, level=None, parent=None):
        self.node = node
        self.level = level
        self.parent = parent


def updateLevelAndParent(root, x, y, level=1, parent=None):
    if root is None:
        return

    updateLevelAndParent(root.left, x, y, level+1, root)

    if root == x.node:
        x.level = level
        x.parent = parent

    if root == y.node:
        y.level = level
        y.parent = parent

    updateLevelAndParent(root.right, x, y, level+1, root)

    


def checkCousins(root, node1, node2):
    if root is None:
        return False

    level = 1
    parent = None

    x = NodeInfo(node1, level, parent)
    y = NodeInfo(node2, level, parent)

    updateLevelAndParent(root, x, y)

    return x.level == y.level and x.parent != y.parent


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if checkCousins(root, root.left.right, root.right.left):
        print('Nodes are cousins to each other')
    else:
        print('Nodes are not cousins to each other')