class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def DFS(graph, arrival, vertex, discovered, bridges, parent, time):
    discovered[vertex] = True
    time = time + 1

    arrival[vertex] = time

    _time = arrival[vertex]

    for u in graph.adjList[vertex]:
        if not discovered[u]:
            _time = min(_time, DFS(graph, arrival, u, discovered, bridges, vertex, time))

        elif u != parent:
            _time = min(_time, arrival[u])

    if arrival[vertex] == _time and parent != -1:
        bridges.add((parent, vertex))

    return _time



def findBridges(graph, n):
    bridges = set()

    discovered = [False] * n
    arrival = [None] * n

    time = 0
    start  = 0
    parent = -1

    DFS(graph, arrival, start, discovered, bridges, parent, time)

    return bridges


if __name__ == '__main__':
    edges = [
        (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)
    ]

    n = 6
    graph = Graph(edges, n)

    bridges = findBridges(graph, n)
    if bridges:
        print(f'The bridges are {bridges}')
    else:
        print('There are no bridges')