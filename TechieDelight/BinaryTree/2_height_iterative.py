from collections import deque

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0    

    queue = deque()
    queue.append(root)

    height = 0

    while queue:
        size = len(queue)

        while size > 0:
            front = queue.popleft()

            if front.left:
                queue.append(front.left)

            if front.right:
                queue.append(front.right)

            size -= 1

        height += 1

    return height

if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    print('The height of the binary tree is', height(root))