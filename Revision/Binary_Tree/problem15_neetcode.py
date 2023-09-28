from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(root):
    if root is None:
        return

    q = deque()

    q.append(root)

    while q:
        node = q.popleft()

        if node:
            q.append(node.left)
            q.append(node.right)

        else:
            while q:
                if q.popleft():
                    return False

    return True


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isBalanced(root):
        print('The binary tree is balanced')
    else:
        print("The binary tree is not balanced")