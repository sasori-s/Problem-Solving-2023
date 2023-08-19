class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(garph, visited, arrival, v, parent, time, bridges):
    time = time + 1
    visited[v] = True
    arrival[v] = time

    t = arrival[v]

    for u in graph.adjList[v]:
        if not visited[u]:
            t = min(t, DFS(graph, visited, arrival, u, v, time, bridges))
        
        elif u != parent:
            t = min(t, arrival[u])

    if arrival[v] == t and parent != -1:
        bridges.add((parent, v))

    return t

def findBridges(graph, n):
    visited = [False] * n
    arrival = [None] * n

    start = 0
    parent = -1
    time = 0

    bridges = set()

    DFS(graph, visited, arrival, start, parent, time, bridges)

    return bridges


if __name__ == '__main__':
    edges = [
        (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)
    ]

    n = 6 

    graph = Graph(edges, n)

    bridges = findBridges(graph, n)

    if bridges:
        print("The bridges are ", bridges)
    else:
        print("The graph is 2-edge connected")