class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(mesg, head):
    print(mesg, end=" ")
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next  
    print('None')

def merge(a, b):
    dummy = Node()
    tail = dummy

    while True:
        if a is None:
            tail.next = None
            break

        if b is None:
            tail.next = a
            break

        else:
            tail.next = a
            tail = tail.next
            a = a.next

            tail.next = b
            tail = tail.next
            b = b.next

    a = dummy.next

    return a, b


if __name__ == '__main__':
    a = b = None

    for i in reversed(range(4)):
            a = Node(i, a)

    for i in reversed(range(4, 11)):
            b = Node(i, b)

    printList("First list: ", a)
    printList("Second list: ", b)

    a, b = merge(a, b)

    print("\nAfter merge")

    printList("First list: ", a)
    printList("Second list: ", b)

