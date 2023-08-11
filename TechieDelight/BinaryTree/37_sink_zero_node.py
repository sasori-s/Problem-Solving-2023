class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def sink(root):
    if root is None:
        return
    
    if root.left and root.left.data:
        temp = root.data
        root.data = root.left.data
        root.left.data = temp

        sink(root.left)

    if root.right and root.right.data:
        temp = root.data
        root.data = root.right.data
        root.right.data = temp

        sink(root.right)

def sinkNodes(root):
    if root is None:
        return 
    
    sinkNodes(root.left)
    sinkNodes(root.right)

    if root.data == 0:
        sink(root)

if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(2)
    root.right.left.left = Node(3)
    root.right.left.right = Node(4)

    sinkNodes(root)
    inorder(root)