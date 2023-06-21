class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    

def rearrange(head):
    if head is None and head.next is None:
        return 
    
    dummyFirst = Node()
    dummySecond = Node()

    first = dummyFirst
    second = dummySecond

    curr = head

    while curr:
        first.next = curr
        first = first.next

        if curr.next:
            second.next = curr.next
            second = second.next
            curr = curr.next
        
        curr = curr.next
        
    first.next = dummySecond.next
    second.next = None
        
if __name__ == "__main__":
    head = None

    for i in reversed(range(5)):
        head = Node(i + 1, head)

    rearrange(head)
    printList(head)
