class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
def printList(msg, head):
    print(msg)
    ptr = head

    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")

def merge(a, b):
    dummy = Node()
    tail = dummy

    while True:
        if a is None:
            tail.next = None
            break

        elif b is None:
            tail.next = a
            break

        else:
            tail.next = a
            tail = a
            a = a.next

            tail.next = b
            tail = b
            b = b.next
    
    a = dummy.next
    return a, b
    
    

if __name__ == "__main__":
    a = b = None

    for i in reversed(range(4)):
        a = Node(i, a)

    for i in reversed(range(4, 11)):
        b = Node(i, b)

    printList("First List : ", a)
    printList("Second List : ", b)

    a, b = merge(a, b)
    print('\nAfter Merge: ')

    printList("First List : ", a)
    printList("Second List : ", b)
    
