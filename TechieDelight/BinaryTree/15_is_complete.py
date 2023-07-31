from collections import deque

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isComplete(root):
    if root is None:
        return False

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

    if isComplete(root):
        print("Complete binary tree")
    else:
        print('Not a complete binary tree')