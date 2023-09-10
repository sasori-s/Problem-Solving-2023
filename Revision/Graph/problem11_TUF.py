from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def DFS(graph, discovered, stack, v):
    discovered[v] = True

    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, discovered, stack, u)

    stack.append(v)


def doTopologicalSort(graph, n):
    discovered = [False] * n
    stack = deque()

    for i in range(n):
        if not discovered[i]:
            DFS(graph, discovered, stack, i)

    answer = []
    while stack:
        answer.append(stack.pop())

    print(answer)



if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)   
    ]

    n = 8

    graph = Graph(edges, n)
    doTopologicalSort(graph, n)