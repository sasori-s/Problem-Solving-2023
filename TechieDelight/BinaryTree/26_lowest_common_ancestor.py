class Node:
    def __init__(self, data=None, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right

def isNodePresent(root, node):
    if root is None:
        return False
    
    if root == node:
        return True

    return isNodePresent(root.left, node) or isNodePresent(root.right, node) 

def findlca(root, lca, x, y):
    if root is None:
        return False, lca
    
    if root == x or root == y:
        return True, root

    left, lca = findlca(root.left, lca, x, y)
    right, lca = findlca(root.right, lca, x, y)

    if left and right:
        lca = root

    return (left or right), lca

    

def findLCA(root, a, b):
    if root is None:
        return
    
    lca = None
    if isNodePresent(root, a) and isNodePresent(root, b):
        lca = findlca(root, lca, a, b)[1]

    if lca:
        print("LCA is, ", lca.data)
    else:
        print("There is no LCA")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    findLCA(root, root.right.left.left, root.right.right)
    findLCA(root, root.right.left.left, Node(10))
    findLCA(root, root.right.left.left, root.right.left.left)
    findLCA(root, root.right.left.left, root.right.left)
    findLCA(root, root.left, root.right.left)