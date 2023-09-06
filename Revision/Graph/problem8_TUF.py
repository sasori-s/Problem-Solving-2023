from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def isBipertite(graph, n):
    color = [-1] * n
    vertex = 0
    color[vertex] = 0

    discovered = [False] * n
    discovered[vertex] = True

    queue = deque()
    queue.append(vertex)

    while queue:
        vertex = queue.popleft()

        for u in graph.adjList[vertex]:
            if color[u] == -1:
                color[u] = not color[vertex]
                queue.append(u)

            elif color[u] == color[vertex]:
                return False

    return True


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]
    n = 9 

    graph = Graph(edges, n)

    if isBipertite(graph, n):
        print('The graph is Bipertite')
    else:
        print('The graph is not Bipertite')

