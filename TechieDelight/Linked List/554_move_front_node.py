class Node:
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

    
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

    print("None")

if __name__ == "__main__":
    a = None

    for i in reversed(range(3)):
        a = Node(i, a)

    b = None

    for i in range(3):
        b = Node(2 * (i + 1), b)

    if b:
        newNode = b
        b = b.next

        newNode.next = a
        a = newNode

    printList(a)
    printList(b)

    
    