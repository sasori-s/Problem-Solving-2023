class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def push(head, data):
    node = Node(data, None, head)
    if head:
        head.prev = node

    head = node
    return head

    

def printDDL(msg, head):
    print(msg, end="")
    itr = head

    while itr:
        print(itr.data, end=" -> ")
        itr = itr.next
    
    print("None")

def swap(node):
    prev = node.prev
    node.prev = node.next
    node.next = prev


def reverseDDL(head):
    prev = None
    curr = head

    while curr:
        swap(curr)
        prev = curr
        curr = curr.prev

    if prev:
        head = prev

    return head

if __name__ == "__main__":
    head = None
    for key in range(1, 6):
        head = push(head, key)
    
    printDDL('Original A: ', head)
    head = reverseDDL(head)
    printDDL("Reverse A: ", head)