from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findNextRight(root, node):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)

        while n > 0:
            n -= 1
            front = queue.popleft()

            if front == node:
                if n == 0:
                    return None

                return queue[0]

            if front.left:
                queue.append(front.left)

            if front.right:
                queue.append(front.right)

    return None

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    right = findNextRight(root, 5)
    if right:
        print(f"The right node is {right}")

    else:
        print("The right node does not exist")