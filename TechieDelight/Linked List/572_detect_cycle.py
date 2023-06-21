class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def detectCycle(head):
    curr = head
    s = set()

    while curr:
        if curr in s:
            return True
        
        s.add(curr)
        curr = curr.next
    
    return False

if __name__ == "__main__":
    head = None

    for i in reversed(range(5)):
        head = Node(i + 1, head)

    head.next.next.next.next.next = head.next.next

    if detectCycle(head):
        print("Cycle Found")
    
    else:
        print("No cycle found")