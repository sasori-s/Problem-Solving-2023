from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findWidth(root):
    if root is None:
        return
    
    q = deque()
    max = 0

    q.append(root)

    while q:
        width = len(q)

        if width > max:
            max = width

        while width > 0:
            curr = q.popleft()
            width = width - 1

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

    print("THe maximum width is ", max)

if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    findWidth(root)