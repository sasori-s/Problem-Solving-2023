import sys
from heapq import heappop, heappush

class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weigth) in edges:
            self.adjList[src].append((dest, weigth))

def findShortestPaths(graph, source, n):
    visited = [False] * n
    pq = []

    heappush(pq, Node(source))
    answer = 0

    while pq:
        node = heappop(pq)
        u = node.vertex

        if visited[u]:
            continue
        else:
            answer += node.weight
            visited[u] = True

            for (v, weight) in graph.adjList[u]:
                if not visited[v]:
                    heappush(pq, Node(v, weight))

    return answer

        

if __name__ == '__main__':
    edges = [
        (0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
            (4, 1, 1), (4, 2, 8), (4, 3, 2)
    ]

    n = 5

    graph = Graph(edges, n)
    print(findShortestPaths(graph, 0, n))