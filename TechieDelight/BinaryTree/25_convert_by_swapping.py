class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = None
        self.left = left
        self.right = right

def equal(X, Y):
    if X == Y:
        return True

    return (X is not None and Y is not None) and (X.data == Y.data) and \
        ((equal(X.left, Y.left) and equal(X.right, Y.right)) or \
        (equal(X.right, Y.left) and equal(X.left, Y.right)))

if __name__ == "__main__":
    X = Node(6)
    X.left = Node(3)
    X.right = Node(8)
    X.left.left = Node(1)
    X.left.right = Node(7)
    X.right.left = Node(4)
    X.right.right = Node(2)
    X.right.left.left = Node(1)
    X.right.left.right = Node(7)
    X.right.right.right = Node(3)

    Y = Node(6)
    Y.left = Node(8)
    Y.right = Node(3)
    Y.left.left = Node(2)
    Y.left.right = Node(4)
    Y.right.left = Node(7)
    Y.right.right = Node(1)
    Y.left.left.left = Node(3)
    Y.left.right.left = Node(1)
    Y.left.right.right = Node(7)
 
    if equal(X, Y):
        print("Binary tree can be converted")
    else:
        print("Binray tree cannot be converted")