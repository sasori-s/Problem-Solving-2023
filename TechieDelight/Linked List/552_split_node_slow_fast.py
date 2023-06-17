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


def frontBackSplit(source):
    if source is None or source.next is None:
        frontRef = source
        backRef = None
        return frontRef, backRef
    
    slow = source
    fast = source.next

    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    frontRef = source
    backRef = slow.next
    slow.next = None

    return frontRef, backRef

if __name__ == "__main__":
    keys = [6, 3, 4, 8, 2, 9]

    head = None

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    first, second = frontBackSplit(head)
    printList("Front List: ", first)
    printList("Back List: ", second)