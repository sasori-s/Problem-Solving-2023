from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def BFS(garph, v, n, discovered):
    queue = deque()
    queue.append(v)

    discovered[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for u in garph.adjList[v]:
            # print(u)
            if not discovered[u]:
                discovered[u] = True
                queue.append(u)



if __name__ == '__main__':
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]

    n = 15

    discovered = [False] * n
    graph = Graph(edges, n)

    for i in range(n):
        # print(f'index {i}')
        if not discovered[i]:
            BFS(graph, i, n, discovered)
