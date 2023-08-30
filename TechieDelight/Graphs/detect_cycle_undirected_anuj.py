class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(v, visited, adj, parent):
    visited[v] = True

    for neighbour in adj[v]:
        if not visited[neighbour]:
            DFS(neighbour, visited, adj, v)

        elif parent != neighbour:
            return True

    return False

def iscycle(V, adj):
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if DFS(i, visited, adj, -1):
                return True

    return False

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11), (5, 9)
    ]

    n = 12
    graph = Graph(edges, n)

    print(iscycle(n, graph.adjList))