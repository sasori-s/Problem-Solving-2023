from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Pair:
    def __init__(self, hd=None, node=None) -> None:
        self.hd = hd
        self.node = node

def topView(root):
    q = deque()
    d = {}

    q.append(Pair(0, root))

    while q:
        curr = q.popleft()

        if d.get(curr.hd) is None:
            d[curr.hd] = curr.node.data

        if curr.node.left:
            q.append(Pair(curr.hd - 1, curr.node.left))

        if curr.node.right:
            q.append(Pair(curr.hd + 1, curr.node.right))

    for key in sorted(d.keys()):
        print(d.get(key), end=" ")

    # return d




if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    # print(topView(root))
    topView(root)