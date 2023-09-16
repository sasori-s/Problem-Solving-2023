from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def printNodes(root):
    q1 = deque()
    q2 = deque()

    d = {}

    level = 1

    d.setdefault(level, []).append(root.data)

    # print(root.data, end=' ')

    if root.left and root.right:
        q1.append(root.left)
        q2.append(root.right)

    while q1:
        n = len(q1)
        level += 1

        for _ in range(n):
            x = q1.popleft()
            # print(x.data, end=" ")

            d.setdefault(level, []).append(x.data)

            if x.left:
                q1.append(x.left)
            
            if x.right:
                q1.append(x.right)


            y = q2.popleft()
            # print(y.data, end=" ")
            d.setdefault(level, []).append(y.data)

            if y.right:
                q2.append(y.right)

            if y.left:
                q2.append(y.left)


    for i in reversed(d.keys()):
        print(d.get(i), end=" ")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    printNodes(root)