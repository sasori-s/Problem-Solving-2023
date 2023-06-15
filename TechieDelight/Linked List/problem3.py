class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print('None')

def appendNode(head, key):
    current = head

    node = Node(key)
    if current is None:
        head = node
    else:
        while current.next:
            current = current.next

        current.next = node
    
    # print(current.data)
    return head

if __name__ == "__main__":
    keys = [1, 2, 3, 4]
    head = None
    for key in keys:
        head = appendNode(head, key)
    
    printList(head)