class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findLCA(root, a, b):
    if root is None:
        return None

    if root == a or root == b:
        return root
    
    left = findLCA(root.left, a, b)
    right = findLCA(root.right, a, b)

    if left is None:
        return right

    if right is None:
        return left

    return root


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    lca_node = findLCA(root, root.right.left.left, root.right.right)
    print("The longest common ancestor is ", lca_node.data)