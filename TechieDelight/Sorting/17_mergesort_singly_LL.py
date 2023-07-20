class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end="->")
        ptr = ptr.next

    print("None")

def frontBackSplit(source):
    if source is None and source.next is None:
        return source, None

    (slow, fast) = (source, source.next)
    
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    ret = (source, slow.next)
    # slow.next = next
    slow.next = None

    return ret

def sortedMerge(a, b):
    if a is None:
        return b
    
    elif b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)

    else:
        result = b
        result.next = sortedMerge(a, b.next)

    return result


def mergesort(head):
    if head is None or head.next is None:
        return head

    front, back = frontBackSplit(head)

    front = mergesort(front)
    back = mergesort(back)

    return sortedMerge(front, back)

if __name__ == "__main__":
    keys = [8, 6, 4, 9, 3, 1]
    
    head = None
    for key in keys:
        head = Node(key, head)

    head = mergesort(head)
    printList(head)