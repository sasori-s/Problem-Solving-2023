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

def removeDuplicates(head):
    current = head

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        
        else:
            current = current.next

    return head


if __name__ == '__main__':
    keys = [1, 2, 2, 2, 3, 4, 4, 5]

    head = None

    for key in reversed(keys):
        head = Node(key, head)

    head = removeDuplicates(head)
    printList(head)