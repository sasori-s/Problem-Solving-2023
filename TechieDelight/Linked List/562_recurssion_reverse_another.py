class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")

def reverse(head):
    if head is None:
        return head
    
    first = head
    rest = first.next

    if rest is None:
        return head
    
    rest = reverse(rest)
    
    first.next.next = first
    first.next = None
    head = rest

    return head

if __name__ == "__main__":
    head = None
    for i in reversed(range(6)):
        head = Node(i + 1, head)
    head = reverse(head)
    printList(head)