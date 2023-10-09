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


def reverseInGroups(head, k):
    if head is None:
        return None

    current = head
    prev = None
    count = 0

    while current and count < k: 
        count += 1
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    head.next = reverseInGroups(current, k)

    return prev



if __name__ == '__main__':
    head = None

    for i in reversed(range(1, 8)):
        head = Node(i, head)

    head = reverseInGroups(head, 3)
    printList("After Reversing: ", head)
