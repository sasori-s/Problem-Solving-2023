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


def deleteNode(head, m, n):
    if head is None or head.next is None:
        return head

    current = head
    prev = None

    for i in range(1, m + 1):
        prev = current
        current = current.next

        if not current:
            return head

    for i in range(1, n + 1):
        if current:
            nextNode = current.next
            current = nextNode
        
    prev.next = nextNode

    deleteNode(current, m, n)

    return head





if __name__ == '__main__':
    head = None

    for i in reversed(range(10)):
        head = Node(i + 1, head)

    head = deleteNode(head, 1, 3)

    printList("After deletation: ", head)