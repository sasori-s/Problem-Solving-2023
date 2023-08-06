class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

def printList(mid):
    while mid and mid.prev:
        mid = mid.prev

    head = mid

    while head:
        print(head.data, end=" ")
        head = head.next

def findVerticalSum(root, curr):
    if not root:
        return

    curr.data += root.data
    
    if root.left and curr.prev is None:
        curr.prev = ListNode(0,None, curr)

    if root.right and curr.next is None:
        curr.next = ListNode(0, curr, None)

    findVerticalSum(root.left, curr.prev)
    findVerticalSum(root.right, curr.next)
    

def printVerticalSum(root):
    if root is None:
        return

    curr = ListNode(0, None, None)
    findVerticalSum(root, curr)
    printList(curr)
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    printVerticalSum(root)