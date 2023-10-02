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

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))


def findRoute(route, vertex, prev):
    if vertex >= 0:
        findRoute(route, prev[vertex], prev)
        route.append(vertex)


def findShortestPath(graph, source, n):
    pq = []
    heappush(pq, Node(source))

    dist = [sys.maxsize] * n
    done = [False] * n
    prev = [-1] * n

    dist[source] = 0
    done[source] = True

    while pq:
        node = heappop(pq)
        u = node.vertex

        for (v, _weight) in graph.adjList[u]: 
            if not done[v] and (dist[u] + _weight < dist[v]):
                dist[v] = dist[u] + _weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        done[u] = True 

    route = []

    # print(done)
    # print(dist)
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            findRoute(route, i, prev)
            print(f"Path {source} -> {i}: Minimum cost = {dist[i]}, Route = {route}")
            route.clear()


if __name__ == '__main__':
    edges = [
        (0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
            (4, 1, 1), (4, 2, 8), (4, 3, 2)
    ]

    n = 5

    graph = Graph(edges, n)

    for source in range(n):
        findShortestPath(graph, source, n)