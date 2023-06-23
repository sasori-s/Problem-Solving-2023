class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


def rearrangeEvenOdd(head):
    even = Node()
    odd = Node()

    evenTail = even
    oddTail = odd

    curr = head

    while curr:
        if curr.data & 1:
            oddTail.next = curr
            oddTail = oddTail.next

        else:
            evenTail.next = curr
            evenTail = evenTail.next
        
        curr = curr.next    

        
    evenTail.next = odd.next
    oddTail.next = None

    return even.next

if __name__ == "__main__":
    head = None
    for i in reversed(range(10)):
        head = Node(i + 1, head)

    head = rearrangeEvenOdd(head)
    printList(head)