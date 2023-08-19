class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

    
def DFS(graph, transitive, root, descendent):
    for child in graph.adjList[descendent]:
        if transitive[root][child] == 0:
            transitive[root][child] = 1

            DFS(graph, transitive, root, child)

if __name__ == '__main__':
    edges = [
        (0, 2), (1, 0), (3, 1)
    ]

    n = 4

    graph = Graph(edges, n)

    transitive = [[0 for i in range(n)] for y in range(n)]

    for v in range(n):
        transitive[v][v] = 1
        DFS(graph, transitive, v, v)

        print(transitive[v])