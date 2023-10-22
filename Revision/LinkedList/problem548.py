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

def sortedInsert(head, newNode):
    dummy = Node()

    dummy.next = head

    current = dummy

    while current.next and current.next.data < newNode.data:
        current = current.next

    newNode.next = current.next
    current.next = newNode

    return dummy.next

if __name__ == "__main__":

    head = None

    keys = [2, 4, 6, 8]

    for key in reversed(keys):
        head = Node(key, head)

    head = sortedInsert(head, Node(5))
    head = sortedInsert(head, Node(9))
    head = sortedInsert(head, Node(1))
    
    printList(head)