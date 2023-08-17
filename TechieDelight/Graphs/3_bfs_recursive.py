from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def recursiveBFS(graph, q, discovered):
    if not q:
        return

    v = q.popleft()
    print(v, end=" ")

    for edge in graph.adjList[v]:
        if not discovered[v]:
            q.append(edge)
            discovered[edge] = True

    recursiveBFS(graph, q, discovered)

if __name__ == '__main__':
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]

    n = 15
    discovered = [False] * n
    
    graph = Graph(edges, n)

    q = deque()

    for i in range(n):
        if not discovered[i]:
            discovered[i] = True
            q.append(i)

            recursiveBFS(graph, q, discovered)