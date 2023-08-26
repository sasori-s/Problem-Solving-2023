class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        self.inDegree = [0] * n

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.inDegree[dest] = self.inDegree[dest] + 1

def findOrderings(graph, visited, path, n):
    for v in range(n):
        if graph.inDegree[v] == 0 and not visited[v]:
            for u in graph.adjList[v]:
                graph.inDegree[u] -= 1

            path.append(v)
            visited[v] = True

            findOrderings(graph, visited, path, n)

            for u in graph.adjList[v]:
                graph.inDegree[u] += 1

            path.pop()
            visited[v] = False

    if len(path) == n:
        print(path)


def printAllTopologicalOrder(graph):
    n = len(graph.adjList)

    visited = [False] * n
    path = []
    findOrderings(graph, visited, path, n)

if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    ]

    n = 8 
    graph = Graph(edges, n)

    printAllTopologicalOrder(graph)