from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Pair:
    def __init__(self, node, hd) :
        self.node = node
        self.hd = hd

def printTopView(root):
    if root is None:
        return None

    q = deque()

    d = {}

    q.append(Pair(root, 0))

    while q:
        curr = q.popleft()
        if curr.hd not in d:
            d[curr.hd] = curr.node.data

        if curr.node.left:
            q.append(Pair(curr.node.left, curr.hd - 1))
        
        if curr.node.right:
            q.append(Pair(curr.node.right, curr.hd + 1))


    for key in sorted(d.keys()):
        print(d[key], end=" ")



def printTopView2(root):
    if root is None:
        return None

    q = deque()

    d = {}

    q.append((root, 0))

    while q:
        (curr, hd) = q.popleft()
        # if hd not in d:
        d[hd] = curr.data

        if curr.left:
            q.append((curr.left, hd - 1))
        
        if curr.right:
            q.append((curr.right, hd + 1))


    for key in sorted(d.keys()):
        print(d[key], end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    printTopView2(root)
 