class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def push(head, key):
    node = Node(key, head)

    if head:
        head.prev = node

    return node

def printDDL(head):
    while head:
        print(head.data, end=' ⇔ ')
        head = head.next

    print("None")

def split(head):
    slow = head
    fast = head.next

    while fast:
        fast = fast.next

        if fast:
            fast = fast.next
            slow = slow.next
    
    return slow

def merge(a, b):
    if a is None:
        return b

    if b is None:
        return a

    if a.data <= b.data:
        a.next = merge(a.next, b)
        a.next.prev = a
        a.prev = None
        return a
    
    else:
        b.next = merge(a, b.next)
        b.next.prev = b
        b.prev = None
        return b

    

def mergesort(head):
    if head is None or head.next is None:
        return head

    a = head
    slow = split(head)
    b = slow.next
    slow.next = None

    a = mergesort(a)
    b = mergesort(b)

    head = merge(a, b)
    return head


if __name__ == "__main__":
    keys = [6, 3, 8, 7, 9, 2, 1]

    head = None
    for key in keys:
        head = push(head, key)
    
    haed = mergesort(head)
    printDDL(head)