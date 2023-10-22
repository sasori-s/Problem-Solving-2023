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


def findKthNode(head, k):
    if head is None:
        return None

    current = head

    for i in range(k):
        if current is None:
            return None

        current = current.next

    while current:
        current = current.next
        head = head.next

    return head


if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]

    head = None

    for i in reversed(keys):
        head = Node(i, head)

    k = 3
    node = findKthNode(head, k)

    if node:
        print(f"K\'th node from the end is {node.data}")