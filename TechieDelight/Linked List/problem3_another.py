class Node:
    next = None

    def __init__(self, data):
        self.data = data

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")


def push(head, data):
    newNode = Node(data)
    newNode.next = head
    
    return newNode

def appendNode(head, key):
    current = head

    if current is None:
        head = push(head, key)
    else:
        while current.next:
            current = current.next

        current.next = push(current.next, key)

    return head

if __name__ == "__main__":
    keys = [1, 2, 3, 4]
    head = None

    for key in keys:
        head = appendNode(head, key)

    printList(head)