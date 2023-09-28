class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findDiameter(root, res=[0]):

    if root is None:
        return - 1

    left = findDiameter(root.left, res)
    right = findDiameter(root.right, res )

    res[0] = max(res[0], 2 + left + right)

    return 1 + max(left, right)

    

    # return 1 + max(findDiameter(root.left), findDiameter(root.right))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print(f'The diameter of the tree is {findDiameter(root)}')