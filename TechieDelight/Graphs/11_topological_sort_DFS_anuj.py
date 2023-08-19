from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def topoSort(V, adj):
    stack = deque()
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            DFS(adj, stack, i, visited)

    while stack:
        print(stack.pop(), end=" ")

def DFS(adj, stack, v, visited):
    visited[v] = True

    for u in adj[v]:
        if not visited[u]:
            DFS(adj, stack, u, visited)

    stack.append(v)

if __name__ == '__main__':
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

    n = 8

    graph = Graph(edges, n)

    topoSort(n, graph.adjList)