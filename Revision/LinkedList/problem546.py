class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" ")
        ptr = ptr.next  

def copyList(head):
    current = head

    dummy = Node()
    tail = dummy

    while current:
        tail.next = Node(current.data, tail.next)
        tail = tail.next
        current = current.next

    return dummy.next

if __name__ == '__main__':
    head = None

    for i in reversed(range(4)):
        head = Node(i + 1, head)

    dup = copyList(head)
    printList(dup)