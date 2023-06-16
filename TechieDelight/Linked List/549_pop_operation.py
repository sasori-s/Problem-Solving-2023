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


def pop(headRef):
    if headRef is None:
        return None
    
    result = headRef.data
    headRef = headRef.next

    print("The popped node is ", result)
    return headRef

if __name__ == "__main__":
    head = None
    for i in reversed(range(1, 5)):
        head = Node(i, head)

    head = pop(head)
    printList(head)