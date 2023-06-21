class Node:
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

def detectCycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    head.next.next.next.next.next = head.next.next    
    
    if detectCycle(head):
        print("Cycle Found")
    
    else:
        print("Cycle not found")