class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end="->")
        ptr = ptr.next
    
    print(None)


def construct(keys):
    head = None

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    return head

if __name__ == "__main__":
    keys = [1, 2, 3, 4]
    head = construct(keys)
    printList(head)