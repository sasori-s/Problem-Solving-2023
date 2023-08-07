from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def diagonalPrint(root):
    q = deque()
    if root is None:
        return

    sentinal = Node(-1)

    while root:
        q.append(root)
        root = root.right

    q.append(sentinal)

    while len(q) != 1:
        front = q.popleft()

        if front != sentinal:
            print(front.data, end=" ")
            
            node = front.left

            while node:
                q.append(node)
                node = node.right   

        else:
            q.append(sentinal)
            print()



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    diagonalPrint(root)