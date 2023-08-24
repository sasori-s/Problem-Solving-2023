import sys
from collections import deque

class Graph:
    def __init__(self, edges, n) :
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
            self.adjList[dest].append((src, weight))

def findMaxCost(graph, src, cost, k):
    q = deque()
    vertices = set([src])

    q.append((src, 0, vertices))

    max_cost = -sys.maxsize

    while q:
        v, cost, vertices = q.popleft()

        if cost > k:
            max_cost = max(max_cost, cost)

        for (dest, weight) in graph.adjList[v]:
            if dest not in vertices:
                s = set(vertices)
                s.add(dest)
                q.append((dest, cost + weight, s))


    return max_cost

if __name__ == '__main__':
    edges = [
        (0, 6, 11), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, -8), (3, 4, 10),
        (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6)
    ]

    n = 8 

    src = 0
    cost = 50

    graph = Graph(edges, n)

    max_cost = findMaxCost(graph, src, cost, n)

    if max_cost != -sys.maxsize:
        print(max_cost)

    else:
        print(f'All path from source have their costs < {cost}')