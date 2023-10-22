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


def reverse(head):
    dummy = Node()
    tail = dummy

    current = head

    while current:
        # tail.next = current
        # nextNode = current.next

        # current.next = None
        # tail = tail.next

        # current = nextNode

        nextNode = current.next
        current.next = tail

        tail = current

        current = nextNode

    return tail




if __name__ == '__main__':
    head = None

    for i in reversed(range(1, 7)):
        head = Node(i, head)

    printList("Main list: ", head)

    head = reverse(head)

    printList("Reversec list: ", head)