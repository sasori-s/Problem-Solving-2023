class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def isLeaf(node):
    return node.left is None and node.right is None
        

def truncate(curr, k, target=0):
    if curr is None:
        return None

    target = curr.data + target 

    curr.left = truncate(curr.left, k, target)
    curr.right = truncate(curr.right, k, target)

    if target < k and isLeaf(curr):
        return None
    
    return curr

if __name__ == "__main__":
    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.right.left = Node(4)
    root.right.right = Node(2)
    root.right.left.left = Node(1)
    root.right.left.right = Node(7)
    root.right.right.right = Node(3)
    
    k = 20
    root = truncate(root, k)
    inorder(root)