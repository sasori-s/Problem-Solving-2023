class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findRight(root, node, node_level, level):
    if root is None:
        return None, node_level

    elif root.data == node:
        return None, level

    elif node_level and node_level == level:
        return root, level

    
    left, node_level = findRight(root.left, node, node_level, level + 1 )

    if left:
        return left, node_level

    return findRight(root.right, node, node_level, level + 1 )
    

def findRightNode(root, node):
    node_level = 0
    return findRight(root, node, node_level, 1)[0]


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    right = findRightNode(root, 5)
    if right:
        print('Right node is', right.data)
    else:
        print('Right node doesn\'t exist')
 