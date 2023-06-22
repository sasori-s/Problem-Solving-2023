class Node:
    def __init__(self, data=None, next = None) -> None:
        self.data = data
        self.next = next

def printList(head):
    ptr = head

    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

def removeDuplicate(head):
    current = head
    prev = None

    s = set()

    while current:
        if current.data in s:
           prev.next = current.next 
        
        else:
            s.add(current.data)
            prev = current

        current = prev.next

    return head


if __name__ == "__main__":
    head = None
    keys = [5, 3, 4, 2, 5, 4, 1, 3]

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    removeDuplicate(head)
    printList(head)