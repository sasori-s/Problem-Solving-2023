class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def findDiameter(root, res):
    if root is None:
        return -1

    left = findDiameter(root.left, res)
    right = findDiameter(root.right, res)

    res[0] = max(res[0], left + right + 2)

    return 1 + max(left, right)


    

if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.right = Node(4)
    # root.right.left = Node(5)
    # root.right.right = Node(6)
    # root.right.left.left = Node(7)
    # root.right.left.right = Node(8)

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(6)
    root.left.left.left = Node(5)

    res = [0]

    # print("The diameter of the tree is " ,findDiameter(root, res))
    findDiameter(root, res)
    print(res)