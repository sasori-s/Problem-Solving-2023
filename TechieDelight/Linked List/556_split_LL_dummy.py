class Node:
    def __init__(self, data=None, next=None):
        self.data =data
        self.next = next

def printList(msg, head):
    print(msg, end="")
    ptr = head

    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")

def alternatingSplit(source):
    adummy = Node()
    atail = adummy
    atail.next = None

    bdummy = Node()
    btail = bdummy
    btail.next = None

    current = source

    while current:
        newNode = current
        current = current.next

        newNode.next = atail.next
        atail.next = newNode

        atail = atail.next

        if current:
            newNode = current
            current = current.next

            newNode.next = btail.next
            btail.next = newNode

            btail = btail.next

    return (adummy.next, bdummy.next)


if __name__ == "__main__":
    head = None
    for i in reversed(range(1, 8)):
        head = Node(i, head)

    first, second = alternatingSplit(head)
    printList("first: ", first)
    printList("second: ", second)
