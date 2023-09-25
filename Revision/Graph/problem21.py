import sys
from collections import deque

class Node:
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    def __hash__(self):
        return hash((self.x, self.y, self.dist))

    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 

def isValid(x, y, N):
    return not (x > N or y > N or x < 0 or y < 0)


def findMinimumSteps(source, dest, N):
    visited = set()
    queue = deque()

    queue.append(source)

    while queue:
        node = queue.popleft()
        x = node.x  
        y = node.y
        dist = node.dist

        if x == dest.x and y == dest.y:
            return dist

        if node not in visited:
            visited.add(node)

            for i in range(len(row)):
                _x = x + row[i]
                _y = y + col[i]

                if isValid(_x, _y, N):
                    queue.append(Node(_x, _y, dist + 1))


    return sys.maxsize
 

if __name__ == '__main__':
    N = 8

    source = Node(0, 7)
    dest = Node(7, 0)

    print(f'The minumum number of steps required is {findMinimumSteps(source, dest, N)}')