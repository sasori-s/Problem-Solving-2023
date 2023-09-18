from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reverseOrderTraversal(root):
    if root is None:
        return

    queue = deque()
    stack = deque()

    queue.append(root)

    while queue:
        current = queue.popleft()

        stack.append(current.data)

        if current.right:
            queue.append(current.right)

        if current.left:
            queue.append(current.left)

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
 
    reverseOrderTraversal(root)