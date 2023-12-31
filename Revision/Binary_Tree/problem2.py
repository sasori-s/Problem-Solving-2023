class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findHeight(root):
    if root is None:
        return 0    

    return 1 + max(findHeight(root.left), findHeight(root.right))


if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    print(f"The height of the binary tree is {findHeight(root)}")