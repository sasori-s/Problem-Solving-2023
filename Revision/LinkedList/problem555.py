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

def moveEven(head):
    odd = head
    even = prev = None

    if head is  None:
        return None

    while odd and odd.next:
        if odd.next:
            newNode = odd.next
            odd.next = odd.next.next

            newNode.next = even
            even = newNode

        prev = odd
        odd = odd.next

    if odd:
        odd.next = even
    else:
        prev.next = even


if __name__ == '__main__':
    head = None

    for i in reversed(range(7)):
        head = Node(i + 1, head )


    printList('before: ', head)
    moveEven(head)
    printList("After : ", head)