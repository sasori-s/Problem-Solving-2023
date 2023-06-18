import heapq
from heapq import heappop, heappush

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __lt__(self, other):
        return self.data < other.data

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

    print("None")

def mergeKLists(lists):
    pq = [x for x in lists]
    heapq.heapify(pq)

    head = last = None

    while pq:
        min = heappop(pq)

        if head is None:
            head = min
            last = min

        else:
            last.next = min
            last = min

        if min.next:
            heappush(pq, min.next)

    return head

if __name__ == "__main__":
    k = 3
    lists = [None] * k

    lists[0] = Node(1)
    lists[0].next = Node(5)
    lists[0].next.next = Node(7)

    lists[1] = Node(2)
    lists[1].next = Node(3)
    lists[1].next.next = Node(6)
    lists[1].next.next.next = Node(9)

    lists[2] = Node(4)
    lists[2].next = Node(8)
    lists[2].next.next = Node(10)

    head = mergeKLists(lists)
    printList(head)
