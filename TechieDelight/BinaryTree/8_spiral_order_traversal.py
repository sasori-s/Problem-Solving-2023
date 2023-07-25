from collections import deque
 
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def spiralOrderTraversal(root):
    if root is None:
        return

    q = deque()
    q.appendleft(root)

    flag = True

    while q:
        nodeCount = len(q)

        if flag:
            while nodeCount > 0:
                curr = q.popleft()
                print(curr.data, end=" ")

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

                nodeCount -= 1

        else:
            while nodeCount > 0:
                curr = q.pop()
                print(curr.data, end=" ")

                if curr.right:
                    q.appendleft(curr.right)

                if curr.left:
                    q.appendleft(curr.left)

                nodeCount -= 1

        flag = not flag
        print()



if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    spiralOrderTraversal(root)