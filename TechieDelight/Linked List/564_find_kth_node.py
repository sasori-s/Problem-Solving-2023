class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

def findKthNode(head, k):
    curr = head

    for i in range(k):
        if curr is None:
            return None
        curr = curr.next

    while curr:
        head = head.next
        curr = curr.next

    return head

if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    head = None

    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    k = 3
    node = findKthNode(head, k)

    if node:
        print('k\'th node from the end is', node.data)
