class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            # self.adjList[dest].append(src)


def DFS(graph, closure, root, descendent):
    for child in graph.adjList[descendent]:
        if closure[root][child] == 0:
            closure[root][child] = 1
            DFS(graph, closure, root, child)


if __name__ == '__main__':
    edges = [
        (0, 2), (1, 0), (3, 1)
    ]

    n = 4

    closure = [[0 for _ in range(n)]for _ in range(n)]
    
    graph = Graph(edges, n)

    for vertex in range(n):
        closure[vertex][vertex] = 1
        DFS(graph, closure, vertex, vertex)

        print(closure[vertex])
    
