class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(msg, head):
    print(msg, end="")
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")

def sortedInsert(a, b):
    dummy = Node()
    tail = dummy

    while a and b:
        if a.data == b.data:
            tail.next = Node(a.data, tail.next)
            tail = tail.next
            a = a.next
            b = b.next
        
        elif a.data < b.data:
            a = a.next
        
        else:
            b = b.next

    
    return dummy.next


if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    a = None
    for i in reversed(range(0, len(keys), 3)):
        a = Node(keys[i], a)

    b = None
    for i in reversed(range(1, len(keys), 2)):
        b = Node(keys[i], b)

    printList('FirstList: ', a)
    printList('secondList: ', b)

    head = sortedInsert(a, b)
    printList("Afer insertion: ", head)