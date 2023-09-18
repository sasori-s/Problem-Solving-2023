class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findAncestors(root, node):
    if root is None:
        return None

    if root == node:
        return root

    left = findAncestors(root.left, node)

    right = False
    if not left:
        right = findAncestors(root.right, node)

    if left or right:
        print(root.data, end=" ")

    return left or right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    node = root.right.left.left

    findAncestors(root, node)