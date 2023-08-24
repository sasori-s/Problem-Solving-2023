import sys

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))

def DFS(graph, discovered, v, time, departure):
    discovered[v] = True

    for (u, w) in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, discovered, u, time, departure)

    departure[v] = time

    time += 1
    return time

def findShortestDistance(graph, source, n):
    departure = [-1] * n
    time = 0
    discovered = [False] * n

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, discovered, i, time, departure)

    cost = [sys.maxsize] * n
    cost[source] = 0

    for i in reversed(range(n)):
        v = departure[i]

        for (u, w) in graph.adjList[v]:
            if cost[v] != sys.maxsize and w + cost[v] < cost[u]:
                cost[u] = cost[v] + w

    for i in range(n):
        print(f"dist({source}, {i}) = {cost[i]}")


if __name__ == '__main__':
    edges = [
        (0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5),
        (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)
    ]

    n = 8

    graph = Graph(edges, n)

    source = 7

    findShortestDistance(graph, source, n)