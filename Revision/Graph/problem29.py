import sys
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))


def DFS(graph, discovered, departure, v, time):
    discovered[v] = True

    for (u, w) in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, discovered, departure, u, time)

    departure[time] = v
    time = time + 1

    return time


def findShortestDistance(graph, n, source):
    time = 0    
    discovered = [False] * n
    cost = [sys.maxsize] * n

    departure = [-1] * n

    cost[source] = 0

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, discovered, departure, i, time)

    for i in reversed(range(n)):
        v = departure[i]

        for (u, w) in graph.adjList[v]:
            if cost[v] != sys.maxsize and (cost[u] > cost[v] + w):
                cost[u] = cost[v] + w

    for i in range(n):
        print(f"Distance from {source} to {i} is {cost[i]}")




if __name__ == '__main__':
    edges = [
        (0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5),
        (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)
    ]
    n = 8

    graph = Graph(edges, n)

    source = 7

    findShortestDistance(graph, n, source)