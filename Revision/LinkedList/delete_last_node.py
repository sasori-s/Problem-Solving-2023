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

def popNode(headRef):
    if headRef is None:
        return None

    current = headRef

    while current.next.next:
        current = current.next
    
    current.next = None

    return headRef

if __name__ == '__main__':

    head = None

    for i in reversed(range(1, 5)):
        head = Node(i, head)

    head = popNode(head)
    printList(head)