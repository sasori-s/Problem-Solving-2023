from collections import deque
class Graph:
    def __init__(self, edges, n) :
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isBipertite(graph):
    v = 0
    visited = [False] * graph.n 
    level = [None] * graph.n

    visited[v] = True

    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        for u in graph.adjList[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

                level[u] = level[v] + 1

            elif level[u] == level[v]:
                return False

    return True
    


if __name__ == '__main__':
    edges = [
        (0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)
    ]

    n = 8
    graph = Graph(edges, n)

    if isBipertite(graph):
        print("The graphh is bipertite")
    else:
        print('The graph is not bipertite')