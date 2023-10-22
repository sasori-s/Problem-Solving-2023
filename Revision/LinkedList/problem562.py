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

def reverse(head, headRef):
    if head is None:
        return headRef

    first = head
    rest = first.next

    if rest is None:
        headRef = first
        return headRef

    headRef = reverse(rest, headRef)

    rest.next = first
    first.next = None

    return headRef


        


if __name__ == "__main__":
    head = None

    for i in reversed(range(1, 5)):
        head = Node(i, head)

    head = reverse(head, head)

    printList("reversed list: ", head)