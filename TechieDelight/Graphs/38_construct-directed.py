from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append((dest))
            self.adjList[dest].append((src))

def BFS(graph, n, vertex):
    visited = [False] * n
    edges = []

    visited[vertex] =True

    q = deque()
    q.append(vertex)

    while q:
        curr = q.popleft()

        for u in graph.adjList[curr]:
            if not visited[u]:
                visited[u] = True
                edges.append((u, curr))
                q.append(u)

    return edges



if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5)
    ]

    n = 6

    graph = Graph(edges, n)
    print(edges)

    vertex = 0 
    edges = BFS(graph, n, vertex)
    print(edges)