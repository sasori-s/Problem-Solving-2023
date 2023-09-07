class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findLevel(root, node, level=0):
    if root is None:
        return False, level

    if root == node:
        return True, level

    
    left, level = findLevel(root.left, node, level+1)
    right, level = findLevel(root.right, node, level+1)

    return (left or right), level


def findLevel1(root, node, level=0):
    if root is None:
        return False, level 

    if root == node:
        return True, level

    left, level = findLevel1(root.left, node, level+1, )
    right, level = findLevel1(root.left, node, level+1, )

    if left or right:
        return (left or right), level


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.right.right = Node(8)

    # print(findLevel(root, root.right.left.left))
    print(findLevel1(root, root.right.right))
    print(findLevel1(root, root.right.right))