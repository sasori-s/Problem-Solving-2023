class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, v, visited):
    visited[v] = True

    for u in graph.adjList[v]:
        if not visited[u]:
            DFS(graph, u, visited)

def isStronglyConnected(graph, n):
    visited = [False] * n

    v = 0

    DFS(graph, v, visited)

    for b in visited:
        if not b:
            return False

    visited = [False] * n

    edges = [(j, i) for i in range(n) for j in range(i)]
    
    reverse_graph = Graph(edges, n)

    DFS(graph, v, visited)

    for b in visited:
        if not b:
            return False

    return True

if __name__ == '__main__':
    edges = [
        (0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)
    ]

    n = 5
    graph = Graph(edges, n)

    if isStronglyConnected(graph, n):
        print("The graph is strongly connected graph")
    else:
        print('The graph is not strongly connected graph')