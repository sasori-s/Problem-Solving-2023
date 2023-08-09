class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printDDL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.right

def convert(root, head):
    if root is None:
        return head

    head = convert(root.right, head)

    root.right = head

    if head:
        head.left = root

    head = root

    return convert(root.left, head)

def convertBT(root):
    head = None

    return convert(root, head)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root = convertBT(root)

    printDDL(root)