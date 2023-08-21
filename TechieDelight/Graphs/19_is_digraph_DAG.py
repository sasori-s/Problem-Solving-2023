class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, visited, departure, v, time):
    visited[v] = True

    for u in graph.adjList[v]:
        if not visited[u]:
            time = DFS(graph, visited, departure, u, time)

    departure[v] = time
    time = time + 1

    return time


def isDAG(graph, n):
    visited = [False] * n
    departure = [None] * n

    time = 0

    for i in range(n):
        if not visited[i]:
            time = DFS(graph, visited, departure, i, time)

    for u in range(n):
        for v in graph.adjList[u]:
            if departure[u] <= departure[v]:
                return False

    return True

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)
    ]

    n = 7

    graph = Graph(edges, n)

    if isDAG(graph, n):
        print("The graph is a DAG")
    else:
        print("The graph is not a DAG")
