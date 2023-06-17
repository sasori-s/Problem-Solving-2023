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


def alternatingSplit(odd, even):
    if odd is None or even is None:
        return
    
    if odd.next:
        odd.next = odd.next.next
    
    if even.next:
        even.next = even.next.next
    
    alternatingSplit(odd.next, even.next)

def split(source):
    if not source:
        return None, None
    
    (aRef, bRef) = (source, source.next)
    alternatingSplit(aRef, bRef)

    return (aRef, bRef)

if __name__ == "__main__":
    head = None
    for i in reversed(range(1, 8)):
        head = Node(i, head)

    first, second = split(head)
    printList("first: ", first)
    printList("second: ", second)
