class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, v, discovered):
    discovered[v] = True

    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

def isStronglyConnected(graph, n):
    for i in range(n):
        discovered = [False] * n

        DFS(graph, i, discovered)

        for vertex in discovered:
            if not vertex:
                return False
            
    return True


if __name__ == '__main__':
    edges = [
        (0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)
    ]

    n = 5

    graph = Graph(edges, n)

    if isStronglyConnected(graph, n):
        print("The graph is strongly connected component")
    else:
        print("The graph is not strongly connected component")