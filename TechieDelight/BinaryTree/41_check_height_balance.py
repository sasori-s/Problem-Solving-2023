class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isHeightBalanced(root, isbalanced=True):
    if root is None or not isbalanced :
        return 0, isbalanced

    left_height, isbalanced = isHeightBalanced(root.left, isbalanced)
    right_height, isbalanced = isHeightBalanced(root.right, isbalanced)

    if abs(left_height - right_height) > 1:
        isbalanced = False

    return  max(left_height, right_height) + 1, isbalanced

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
 
    if isHeightBalanced(root)[1]:
        print("The binary tree is balanced")

    else:
        print("The binary tree is not balanced")