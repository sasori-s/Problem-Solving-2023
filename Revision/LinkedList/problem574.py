class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):    
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next  
    print('None')



def sortList(head):
    first = Node()
    second = Node()
    third = Node()

    zero = first
    one = second
    two = third

    current = head

    while current:
        if current.data == 0: 
            zero.next = current
            zero = zero.next

        elif current.data == 1:
            one.next = current
            one = one.next

        else:
            two.next = current
            two = two.next

        current = current.next

    zero.next = second.next if second.next else third.next
    one.next = third.next
    two.next = None

    return first.next


if __name__ == '__main__':
    keys = [1, 2, 0, 0, 1, 2, 1, 2, 1]

    head = None

    for key in reversed(keys):
        head = Node(key, head)

    head = sortList(head)

    printList(head)