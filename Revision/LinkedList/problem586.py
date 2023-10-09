class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def printDDL(msg, head):
    print(msg, end=" ")

    ptr = head
    while ptr:
        print(ptr.data, end=" <--> ")
        ptr = ptr.next

    print('None')


def push(head, key):
    node = Node(key, None, head)

    if head:
        head.prev  = node
    head = node
    return head


def swap(node):
    prev = node.prev
    node.prev = node.next
    node.next = prev


def reverseDDL(head):
    current = head
    prev = None

    while current:
        swap(current)

        prev = current

        current = current.prev

    if prev:
        head = prev

    return head


if __name__ == '__main__':
    head = None

    for key in reversed(range(1, 6)):
        head = push(head, key)

    printDDL("Original list: ", head)

    head = reverseDDL(head)
    print(head.data)

    printDDL("Reversed list: ", head)
    