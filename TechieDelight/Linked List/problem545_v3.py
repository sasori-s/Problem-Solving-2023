class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def push(head, data):
    newNode = Node(data)
    newNode.next = head  
    return newNode

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end = " -> ")
        ptr = ptr.next

    print("None")      


def constructList(keys):
    dummy = Node()
    tail = dummy

    for key in keys:
        tail.next = push(tail.next, key)
        tail = tail.next

    return dummy.next

if __name__ == "__main__":
    keys = [1, 2, 3, 4]
    head = constructList(keys)
    printList(head)