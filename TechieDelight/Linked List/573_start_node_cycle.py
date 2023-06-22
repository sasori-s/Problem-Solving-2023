class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def detectCycle(head):
    if head is None and head.next is None:
        return None

    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head

            while start != slow:
                start = start.next
                slow = slow.next

            return start
        
    return None



if __name__ == "__main__":
    keys = [1, 2 ,3 ,4]
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)
    
    head.next.next.next.next = head.next
    
    start = detectCycle(head)

    if start:
        print("Cycle found starting from node, ", start.data)
    else:
        print("This Linked List does'\t contain any cycle")