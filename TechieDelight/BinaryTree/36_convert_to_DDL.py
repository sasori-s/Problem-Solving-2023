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

    head = convert(root.left, head)
    root.left = None
    right = root.right

    root.right = head

    if head:
        head.left = root

    head = root

    return convert(right, head)

def reverse(head):
    prev = None
    current = head

    while current:
        temp = current.left
        current.left = current.right
        current.right = temp

        prev = current
        current = current.left

    return prev


def convertToDDL(root):
    head = None
    head = convert(root, head)

    head = reverse(head)
    printDDL(head)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    convertToDDL(root)