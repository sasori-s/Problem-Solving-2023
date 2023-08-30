class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def hamiltonianPaths(graph, visited, path, v):
    if len(path) == n:
        print(path)
        return

    for u in graph.adjList[v]:
        if not visited[u]:
            visited[u] = True
            path.append(u)

            hamiltonianPaths(graph, visited, path, u)

            visited[u] = False
            path.pop()

def findHamltonianPaths(graph, n):
    for start in range(n):
        visited = [False] * n
        path = [start]

        visited[start] = True

        hamiltonianPaths(graph, visited, path, start)

if __name__ == "__main__":
    edges = [
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
    ]

    n = 4

    graph = Graph(edges, n)

    findHamltonianPaths(graph, n)