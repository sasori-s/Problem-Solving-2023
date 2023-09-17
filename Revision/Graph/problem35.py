class Graph:
    def __init__(self, edges, n) :
        self.adjList = [[] for _ in range(n)]

        self.indegree = [0] * n

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

            self.indegree[dest] = self.indegree[dest] + 1


def printPaths(graph, discovered, path, n):
    for v in range(n):
        # print(path)
        if graph.indegree[v] == 0 and not discovered[v]:
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] - 1

            path.append(v)
            discovered[v] = True
            # print(path)

            printPaths(graph, discovered, path, n)

            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] + 1

            # print(path)
            path.pop()
            discovered[v] = False

    if len(path) == n:
        print(path)




def findAllTopologicalOrder(graph, n):
    discovered = [False] * n
    path = []

    printPaths(graph, discovered, path, n)


if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    ]

    n = 8

    graph = Graph(edges, n)
    # print(graph.indegree)

    findAllTopologicalOrder(graph, n)