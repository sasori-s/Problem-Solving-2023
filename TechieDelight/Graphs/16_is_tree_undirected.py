class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, visited, parent):
    visited[v] = True

    for u in graph.adjList[v]:
        if not visited[u]:
            if not DFS(graph, u, visited, v):
                return False

        elif u != parent:
            return False

    return True

def isTree(graph, n):
    visited = [False] * n

    isTree = True

    isTree = DFS(graph, 0, visited, -1)

    for i in range(n):
        if not visited[i]:
            return False
        
    return isTree

if __name__ == '__main__':
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)
    ]

    n = 6 
    graph = Graph(edges, n)

    if isTree(graph, n):
        print("The graph is a tree")
    else:
        print("The graph is not a tree")