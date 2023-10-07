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
    current = dummy
    dummy.next = head

    while current.next and current.next.data < newNode.data:
        current = current.next

    newNode.next = current.next
    current.next = newNode

    return dummy.next

def insertSort(head):
    result = None
    current = head

    while current:
        next = current.next
        result = sortedInsert(result, current)

        current = next

    return result

if __name__ == '__main__':
    keys = [6, 3, 4, 8, 2, 9]

    head = None

    for key in reversed(keys):
        head = Node(key, head)

    head = insertSort(head)
    printList(head)