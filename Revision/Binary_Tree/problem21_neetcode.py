class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def checkSubtree(root, sub_root):
    if sub_root is None:
        return True

    if root is None:
        return False

    if root == sub_root:
        if sameTree(root, sub_root):
            return True

    return (checkSubtree(root.left, sub_root) or checkSubtree(root.right, sub_root))


def sameTree(root, sub_root):
    if not root and not sub_root: 
        return True

    if root and sub_root and root.data == sub_root.data:
        return (sameTree(root.left, sub_root.left) and sameTree(root.right, sub_root.right))

    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if checkSubtree(root, root.right):
        print("Subtree")
    else:
        print("Not subtree")