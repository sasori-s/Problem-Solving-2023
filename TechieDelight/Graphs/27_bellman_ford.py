import sys
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))



def runBellman(graph, n):
    dist = [sys.maxsize] * n


if __name__ == "__main__":
    edges = [
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]

    n = 5
    graph = Graph(edges, n)


    runBellman(graph, n)