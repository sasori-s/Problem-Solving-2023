class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next  
    print('None')


def moveNode(head):
    curremt = head

    while curremt.next:
        prev = curremt
        curremt = curremt.next

    curremt.next = head
    head = curremt
    prev.next = None

    return head


if __name__ == '__main__':
    head = None

    for i in reversed(range(1, 5)):
        head = Node(i, head)

    printList(head)

    head = moveNode(head)

    printList(head)


