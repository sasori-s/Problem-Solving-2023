from collections import deque
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isComplete(root):
    if root is None:
        return True

    q = deque()
    flag = False

    while q:
        front = q.popleft()

        if flag and (front.left and front.right):
            return False

        if front.left is None and front.right:
            return False

        if front.left:
            q.append(front.left)

        else:
            flag = True

        if front.right:
            q.append(front.right)

        else:
            flag = True

    return True

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isComplete(root):
        print("THe binary tree is complete")
    else:
        print("The tree is not complete")