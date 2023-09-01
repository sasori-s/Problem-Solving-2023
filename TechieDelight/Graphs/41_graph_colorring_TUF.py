class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isSafe(graph, node, col, n, k, color):
    for u in graph.adjList[node]:
        if color[u] == col:
            return False

    return True

def solve(node, graph, n, k, color):
    if node == n:
        return True

    for i in range(1, k+1):
        if isSafe(graph, node,  i, n, k, color):
            color[node] = i

            if solve(node + 1, graph, n, k, color):
                return True

    return False

def graphColoring(graph, n, k):
    color = [None] * n

    if solve(0, graph, n, k, color):
        return True

    return False

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)
    ]

    n = 6
    k = 3

    graph = Graph(edges, n)

    print(graphColoring(graph, n, k))