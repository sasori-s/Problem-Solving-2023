class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, visited, recursion_stack, v):
    visited[v] = True
    recursion_stack[v] = True


    for u in graph.adjList[v]: 
        if not visited[u]:
            if DFS(graph, visited, recursion_stack, u):
                return True

            elif recursion_stack[u]:
                return True

        recursion_stack[v] = False
        return False

def isDAG(graph, n):
    visited = [False] * n
    recursion_stack = [False] * n

    for i in range(n):
        if not visited[i]:
            if DFS(graph, visited, recursion_stack, i):
                return False

    return True

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)
    ]

    n = 7

    graph = Graph(edges, n)

    if isDAG(graph, n):
        print('The graph is DAG')
    else:
        print("The graph is not DAG")
