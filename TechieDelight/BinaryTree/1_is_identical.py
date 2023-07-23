class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isIndentical(x, y):
    if x is None and y is None:
        return True

    return (x is not None and y is not None) and (x.data == y.data) and \
        isIndentical(x.left, y.left) and isIndentical(x.right, y.right) 

if __name__ == "__main__":
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)

    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)

    if isIndentical(x, y):
        print("The given binary trees are identical")
    else:
        print("The Binary trees are not identical")