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

        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def findShortestPaths(graph, source, n):
    pq = []
    heappush(pq, Node(source))

    dist = [sys.maxsize] * n

    dist[source] = 0

    done = [False] * n
    done[source] = True
    
    prev = [-1] * n

    while pq:
        node = heappop(pq)
        u = node.vertex

        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = (dist[u] + weight)
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        done[u] = True

    route = []

    for i in range(n):
        if i!= source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            print(f"Path ({source} -> {i}): Minimum cost = {dist[i]}, Route= {route}")
            route.clear()



if __name__ == '__main__':
    edges = [
        (0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
            (4, 1, 1), (4, 2, 8), (4, 3, 2)
    ]

    n = 5

    graph = Graph(edges, n)

    for source in range(n):
        findShortestPaths(graph, source, n)