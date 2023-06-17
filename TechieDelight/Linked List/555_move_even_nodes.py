class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(msg, head):
    print(msg, end="")
    ptr = head

    # print("runs 1st time")
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    
    print("None")

def rearrange(head):
    if head is None:
        return
    
    odd = head
    even = prev = None

    while odd and odd.next:
        if odd.next:
            newNode = odd.next
            odd.next = odd.next.next

            newNode.next = even
            even = newNode

        prev = odd
        odd = odd.next

    if odd:
        odd.next = even
    else:
        prev.next = even
    



if __name__ == "__main__":
    head = None
    for i in reversed(range(7)):
        head = Node(i + 1, head)
    
    printList("before: ", head)
    rearrange(head)
    printList("after: ", head)