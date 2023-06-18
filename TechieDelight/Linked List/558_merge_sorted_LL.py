class Node:
    def __init__(self, data=None, next=None):
        self.data =data
        self.next = next

def printList(msg, head):
    print(msg, end="")
    ptr = head

    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")

def sortedMerge(a, b):
    dummy = Node()
    tail = dummy

    while True:
        if a is None:
            tail.next = b
            break

        elif b is None:
            tail.next = a
            break

        if a.data <= b.data:
            if a:
                newNode = a
                a = a.next

                newNode.next = tail.next
                tail.next = newNode

        elif b:
            newNode = b
            b = b.next

            newNode.next = tail.next
            tail.next = newNode
        
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    a = b = None
    for i in reversed(range(1, 8, 2)):
        a = Node(i, a)
 
    for i in reversed(range(2, 7, 2)):
        b = Node(i, b)
 
    # print both lists
    printList('First List: ', a)
    printList('Second List: ', b)
 
    head = sortedMerge(a, b)
    printList('After Merge: ', head)
  