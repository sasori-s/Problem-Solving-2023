class Node:
    def __init__(self,key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def solve(root):
    if root is None:
        return 0

    left = solve(root.left)
    right = solve(root.right)

    node = root.key 
    root.data = left + right

    return left + right + node


def toSumTree(root):
    solve(root)

if __name__ == "__main__":
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    toSumTree(root)