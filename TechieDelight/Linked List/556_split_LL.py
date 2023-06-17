class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(msg, head):
    print(msg, end="")

    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")

def alternatingSplit(head):
    current = head
    a = None
    b = None

    while current:
        newNode = current
        current = current.next

        newNode.next = a
        a = newNode

        if current:
            newNode = current
            current = current.next

            newNode.next = b
            b = newNode

    return(a, b)


if __name__ == "__main__":
    head = None

    for i in reversed(range(7)):
        head = Node(i + 1, head)

    first, second = alternatingSplit(head)
    printList("first : ", first)
    printList("second : ", second)
    