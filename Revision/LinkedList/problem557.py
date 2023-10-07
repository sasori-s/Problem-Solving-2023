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
            tail.next = b
            break

        elif b is None:
            tail.next = a
            break

        else:
            tail.next = a
            tail = a
            a = a.next

            tail.next = b
            tail = b
            b = b.next

    return dummy.next

        


if __name__ == '__main__':
    head = None

    a = b = None

    for i in reversed(range(1, 8, 2)):
        a = Node(i, a)

    for i in reversed(range(2, 7, 2)):
        b = Node(i , b)

    printList("FirstList ", a)
    printList("SecondList ", b)

    head = merge(a, b)

    printList("After Merge ", head)