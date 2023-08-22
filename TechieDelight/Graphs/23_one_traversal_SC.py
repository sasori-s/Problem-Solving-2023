class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, v, visited, arrival, isSC, time):
    if not isSC:
        return 0, False, time

    time += 1

    visited[v] = True
    arrival[v] = time

    arr = arrival[v]

    for w in graph.adjList[v]:
        if not visited[w]:
            _arr, isSC, time = DFS(graph, w, visited, arrival, isSC, time)

            arr = min(arr, _arr)

        else:
            arr = min(arr, arrival[w])

    
    if v and arrival[v] == arr:
        isSC = False

    return arr, isSC, time

def isStronglyConnected(graph, n):
    visited = [False] * n
    arrival = [0] * n

    isSC = True
    time = -1

    isSC = DFS(graph, 0,  visited, arrival, isSC, time)[1]

    for i in range(n):
        if not visited[i]:
            isSC = False

    return isSC

if __name__ == "__main__":
    edges = [
        (0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)
    ]

    n = 5

    graph = Graph(edges, n)

    if isStronglyConnected(graph, n):
        print('The graph is strongly connected graph')
    else:
        print('The graph is not strongly connected graph')