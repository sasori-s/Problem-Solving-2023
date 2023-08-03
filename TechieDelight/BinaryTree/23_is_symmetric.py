class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isSymmetric(X, Y):
    if X is None and Y is None:
        return True

    return (X is not None and Y is not None ) and \
        isSymmetric(X.left, Y.right) and \
        isSymmetric(X.right, Y.left)

def isSymmetricTree(root):
    if root is None:
        return True

    return isSymmetric(root.left, root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
 
    if isSymmetricTree(root):
        print("The Binary tree is symmetric")
    else:
        print("The tree is not symmetric")