class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def DFS(graph, v, n, discovered, arrival, departure, time):
    time = time + 1
    arrival[v] = time

    discovered[v] = True

    for u in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, n, discovered, arrival, departure, time)

    time = time + 1

    departure[v] = time
    
    return time


if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
    n = 8

    graph = Graph(edges, n)

    discovered = [False] * n
    arrival = [None] * n
    departure = [None] * n
    time = -1

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, n, discovered, arrival, departure, time)

    for i in range(n):
        print(f'Vertex {i} {(arrival[i], departure[i])}')