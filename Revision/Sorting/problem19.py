class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def printDDL(msg, head):
    print(msg, end=" ::: ")

    ptr = head
    while ptr:
        print(ptr.data, end=" <-> ")
        ptr = ptr.next

    print("None")


def push(key, head):
    node = Node(key, head)

    if head:
        head.prev = node

    return node


def split(source):
    slow = source
    fast = source.next

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



def mergeSort(head):
    if head is None or head.next is None:
        return head

    a = head
    slow = split(head)
    b = slow.next
    slow.next = None

    a = mergeSort(a)
    b = mergeSort(b)

    head = merge(a, b)

    return head


if __name__ == '__main__':
    keys = [6, 4, 8, 7, 9, 2, 1]

    head = None

    for key in keys:
        head = push(key, head)

    printDDL('Before sorting', head)

    head = mergeSort(head)
    printDDL("After sorting", head)