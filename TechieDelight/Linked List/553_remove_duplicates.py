class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    # print(msg, end="")
    ptr = head
    while ptr:
        print(ptr.data, end = " -> ")
        ptr = ptr.next

    print("None")

def removeDuplicates(head):
    if head is None:
        return None
    
    current = head

    while current.next:
        if current.data == current.next.data:
            nextNext = current.next.next
            current.next = nextNext
        else:
            current = current.next

    return head



if __name__ == "__main__":
    keys = [1, 2, 2, 2, 3, 4, 4, 5]
    head = None

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)    
        
    head = removeDuplicates(head)
    printList(head)