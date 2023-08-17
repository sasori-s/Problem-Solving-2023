class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, discovered, color, v):
    for u in graph.adjList[v]:
        if not discovered[v]:
            discovered[u] = True
            color[u] = not color[v]

            if not DFS(graph, discovered, color, u):
                return False

        elif color[u] == color[v]:
            return False

    return True

def isBipertite(graph, n):
    discovered = [False] * n
    color = [False] * n

    src = 0
    discovered[src] = True
    color[src] = False

    return DFS(graph, discovered, color, src)



if __name__ == '__main__':
    edges = [
        (0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8), (1, 3)
    ]

    n = 9
    graph = Graph(edges, n) 

    if isBipertite(graph, n):
        print("The graph is bipertite")
    else:
        print('The graph is not bipertite')