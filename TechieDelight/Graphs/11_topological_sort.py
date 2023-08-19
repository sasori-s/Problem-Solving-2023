class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, discovered, deaprture, v, time):
    discovered[v] = True
    time += 1

    for u in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, discovered, deaprture, u, time)

    deaprture[time] = v
    time += 1

    return time


def topologicalSort(graph, n):
    departure = [-1] * 2 * n
    time = 0
    discovered = [False] * n

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, discovered, departure, i, time)

    for i in reversed(range(2 * n)):
        if departure[i] != -1:
            print(departure[i], end=" ")

if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    ]

    n = 8
    graph = Graph(edges, n)
    topologicalSort(graph, n)