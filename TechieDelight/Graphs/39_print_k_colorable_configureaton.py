class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isSafe(graph, color, v, c):
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
        
    return True

def kColorable(graph, color, n, v, k):
    if v == n:
        print([COlORS[color[v]] for v in range(n)])
        return

    for c in range(1, k + 1):
        if isSafe(graph, color, v, c):
            color[v] = c

            kColorable(graph, color, n, v + 1, k)

            color[v] = 0
        

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)
    ]

    COlORS = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE']

    n = 6

    graph = Graph(edges, n)

    k = 3

    color = [None] * n

    kColorable(graph, color, n, 0, k)