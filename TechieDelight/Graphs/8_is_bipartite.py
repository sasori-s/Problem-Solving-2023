from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def isBipertite(V, adj):
    color = [-1] * V

    for i in range(V):
        if color[i] == -1:
            if not check(i, V, adj, color):
                return False

    return True

def check(start, V, adj, color):
    q = deque()

    q.append(start)
    color[start] = 0

    while q:
        vertex = q.popleft()

        for ed in adj[vertex]:
            if color[ed] == -1:
                color[ed] = 1 - color[vertex]
                q.append(ed)

            elif color[ed] == color[vertex]:
                return False

    return True
            
if __name__ == '__main__':
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]
    n = 9

    graph = Graph(edges, n)

    print(isBipertite(n, graph.adjList))