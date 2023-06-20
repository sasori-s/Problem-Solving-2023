class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')

def deleteNodes(head, m, n):
    if head is None or head.next is None:
        return head
    
    prev = None
    curr = head

    for i in range(1, m + 1):
        prev = curr
        curr = curr.next

        if not curr:
            return head
        
    for i in range(1, n + 1):
        if curr:
            next = curr.next
            curr = next

    prev.next = curr

    deleteNodes(curr, m, n)
    return head



if __name__ == "__main__":
    head = None
    for i in reversed(range(10)):
        head = Node(i + 1, head)
 
    head = deleteNodes(head, 1, 3)
    printList(head)