from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def isReachable(graph, visited, path, src, dest):
    visited[src] = True

    path.append(src)

    if src == dest:
        return True

    for i in graph.adjList[src]:
        if not visited[i]:
            if isReachable(graph, visited, path, i, dest):
                return True

    path.pop()
    return False

if __name__ == '__main__':
    edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]

    n = 8
    graph = Graph(edges, n)

    visited = [False] * n

    path = deque()

    (src, dest) = (0, 7)

    if isReachable(graph, visited, path, src, dest):
        print(f"Path exits from {src} vertex to {dest} vertex")
        print(f"The path is", list(path))

    else:
        print(f"No path exists betweem {src} and {dest} vertex")