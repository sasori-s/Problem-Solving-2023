class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
def rearrange(head):
    if head is None:
        return None

    prev = head
    curr = head.next

    while curr:
        if prev.data > curr.data:
            temp = prev.data
            prev.data = curr.data
            curr.data = temp

        if curr.next and curr.next.data > curr.data:
            temp = curr.next.data
            curr.next.data = curr.data
            curr.data = temp

        if curr.next is None:
            break
        
        curr = curr.next.next

    return head



if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 6]

    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    head = rearrange(head)
    printList(head)