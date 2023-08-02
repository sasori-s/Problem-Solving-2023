class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def is_Sublist(x, y):
    for i in range(len(x) - len(y) + 1):
        if x[i: i + len(y)] == y:
            return True
    return False

def inorder(node, list):
    if node is None:
        return 
    inorder(node.left, list)
    list.append(node.key)
    inorder(node.right, list)

def postOrder(node, list):
    if node is None:
        return

    postOrder(node.left, list)
    postOrder(node.right, list)
    list.append(node.key)

def checkSubtree(main, subtree):
    if main is None:
        return False

    if main == subtree:
        return True

    first = []
    second = []

    inorder(main, first)
    inorder(subtree, second)

    if not is_Sublist(first, second):
        return False
    
    first.clear()
    second.clear()

    postOrder(main, first)
    postOrder(subtree, second)

    if not is_Sublist(first, second):
        return False

    return True

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if checkSubtree(root, root.right):
        print("Yes")
    else:
        print('No')