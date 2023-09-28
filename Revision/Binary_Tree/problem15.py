from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    flag = False

    while queue:
        node = queue.popleft()

        if flag and (node.left or node.right):
            return False

        if node.left is None and node.right:
            return None

        if node.left:
            queue.append(node.left)
        else:
            flag = True

        if node.right:
            queue.append(node.right)
        else:
            flag = True

    return True


if __name__ == '__main__':
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