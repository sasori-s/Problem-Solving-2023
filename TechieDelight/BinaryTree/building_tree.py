class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def createTree():
    # root = Node()
    data = int(input("Enter the node's data "))

    if data == -1:
        return None

    root = Node(data)

    print(f"Enter to left of {data} Node")
    root.left = createTree()

    print(f"Enter to right of {data} Node")
    root.right = createTree()
    
    return root
    # root = Node(data)

def preorder(root):
    if root == None:
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

if __name__ == "__main__":
    root = createTree()