class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(msg ,head):
    print(msg, end="")
    ptr = head
    while ptr:
        print(ptr.data, end = " -> ")
        ptr = ptr.next

    print("None")


def findLength(head):
    count = 0
    ptr = head

    while ptr:
        count = count + 1
        ptr = ptr.next

    return count

def frontBackSplit(source):
    length = findLength(source)

    if length < 2:
        frontRef = source
        backRef = None

        return frontRef, backRef
    
    current = source

    hopCount = (length - 1) // 2

    for i in range(hopCount):
        current = current.next

    frontRef = source
    backRef = current.next
    current.next = None

    return frontRef, backRef

if __name__ == "__main__":
    keys = [6, 3, 4, 8, 2, 9]
    head = None

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    first, second = frontBackSplit(head)
    printList("Front List: ", first)
    printList("Back List: ", second)