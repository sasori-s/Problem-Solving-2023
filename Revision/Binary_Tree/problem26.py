class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isNodePresent(root, node):
    if root is None:
        return False

    if node == root:
        return True

    return isNodePresent(root.left, node) or isNodePresent(root.right, node)


def LCA(root, lca, x, y):
    if root is None:
        return  False, lca

    if root == x or root == y:
        return True, root

    left, lca = LCA(root.left, lca,x, y)
    right, lca = LCA(root.right, lca,x, y)

    if left and right:
        lca = root

    return (left or right), lca



def findLCA(root, x, y):
    lca = None

    if isNodePresent(root, x) and isNodePresent(root, y):
        lca = LCA(root, lca, x, y)[1]

    if lca:
        print(f"The LCA is {lca.data}")
    else:
        print("LCA does not exist")


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    findLCA(root, root.right.left.left, root.right.right)