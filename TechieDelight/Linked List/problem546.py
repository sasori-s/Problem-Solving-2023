class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

    print("None")        

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    node = [None] * len(A)

    for i in range(len(A)):
        node[i] = Node(A[i], None)

        if i > 0:
            node[i - 1].next = node[i]

    head = node[0]
    printList(head)
