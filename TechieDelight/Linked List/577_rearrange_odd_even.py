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
    odd = None
    oddTail = None

    even = None
    evenTail = None

    curr = head

    while curr:
        if curr.data & 1:
            if odd is None:
                odd = oddTail = curr

            else:
                oddTail.next = curr
                oddTail = oddTail.next

        else:
            if even is None:
                even = evenTail = curr
            
            else:
                evenTail.next = curr
                evenTail = evenTail.next

        curr = curr.next


    if even:
        head = even
        evenTail.next = odd

    else:
        head = odd
    
    if oddTail:
        oddTail.next = None
    
    return head

if __name__ == "__main__":
    head = None
    for i in reversed(range(10)):
        head = Node(i + 1, head)

    head = rearrangeEvenOdd(head)
    printList(head)