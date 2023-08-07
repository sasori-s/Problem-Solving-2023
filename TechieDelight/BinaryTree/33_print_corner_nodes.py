from collections import deque
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printTree(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)

    while q:
        size = len(q)
        n = size

        while n:
            n = n - 1
            node = q.popleft()

            if n == size - 1 or n == 0:
                print(node.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        print()

    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.right.left.left = Node(8)
    root.right.left.right = Node(9)
    root.right.right.right = Node(10)
    
    printTree(root)