class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printVerticalSum(root, dist, d):
    if root is None:
        return
    
    d[dist] = d.get(dist, 0) + root.data

    printVerticalSum(root.left, dist - 1, d)
    printVerticalSum(root.right, dist + 1, d)


def printVertical(root):
    if root is None:
        return 
    
    d = {}

    printVerticalSum(root, 0, d)

    for key in sorted(d.keys()):
        print(d.get(key), end=" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printVertical(root)