class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(meg, head):
    ptr = head
    print(meg, end=" ::: ")

    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

    print("None")


def frontBackSplit(source):
    if source is None or source.next is None:
        return source, None

    (slow, fast) = (source, source.next)

    while fast:
        fast = fast.next

        if fast:
            fast = fast.next
            slow = slow.next

    ret = (source, slow.next)    
    slow.next = None

    return ret


def sortedMerge(a, b):
    if a is None:
        return b
    
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)

    else:
        result = b
        result.next = sortedMerge(a, b.next)

    return result
    


def mergeSort(head):
    if head is None or head.next is None:
        return head

    front, back = frontBackSplit(head)

    front = mergeSort(front)
    back = mergeSort(back)

    return sortedMerge(front, back)


if __name__ == '__main__':
    keys = [8, 6, 4, 9, 3, 1]

    head = None

    
    for key in keys:
        head = Node(key, head)
    
    printList("Before sorting", head)
    
    head = mergeSort(head)
    printList("After sorting", head)