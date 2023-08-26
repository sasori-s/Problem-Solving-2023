import sys
from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def isReachable(graph, source, dest):
    n = len(graph.adjList)
    discovered = [False] * n

    discovered[source] = True
    q = deque()
    q.append(source)

    while q:
        v = q.popleft()

        if v == dest:
            return True

        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)

    return False

if __name__ == "__main__":
    edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]

    n = 8 

    graph = Graph(edges, n)

    (source, dest) = (0,7)

    if isReachable(graph, source, dest):
        print(f"Path exists between {source} to vertex {dest}")
    else:
        print(f"No path exists between vertices {source} and {dest}")