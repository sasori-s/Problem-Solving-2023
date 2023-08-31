from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def BFS(graph, src, n, parent=-1):
    q = deque()
    q.append((src, -1))

    visited = [False] * n

    visited[src] = True
        
    while q:
        (v, parent) = q.popleft()

        for u in graph.adjList[v]:
            if not visited[u]:
                visited[u] = True
                q.append((u, v))

            elif u != parent:
                return True

    return False

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11), (5, 9)
    ]

    n = 12

    graph = Graph(edges, n)

    if BFS(graph, 0, n):
        print('The graph contains cycle')

    else:
        print('The graph does not contain any cycle')