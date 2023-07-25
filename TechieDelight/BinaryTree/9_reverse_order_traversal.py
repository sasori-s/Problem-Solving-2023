from collections import deque

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def reverseLevelOrderTraversal(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    stack = deque()

    while queue:
        curr = queue.popleft()
        stack.append(curr.key)

        if curr.right:
            queue.append(curr.right)

        if curr.left:
            queue.append(curr.left)

    while stack:
        print(stack.pop(), end=" ")

if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    reverseLevelOrderTraversal(root)