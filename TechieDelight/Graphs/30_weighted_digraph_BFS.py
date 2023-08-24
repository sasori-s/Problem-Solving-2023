from collections import deque

class Graph:
    def __init__(self, edges, n, x):
        self.adjList = [[] for _ in range(3 * n)]

        for (v, u, weight) in edges:
            if weight == 3*x:
                self.adjList[v].append(v + n)
                self.adjList[v].append(v + 2 * n)
                self.adjList[v + 2 * n].append(u)

            elif weight == 2*x:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(u)

            else:
                self.adjList[v].append(u)

def printPath(predecessor, v, cost, n):
    if v >= 0:
        cost = printPath(predecessor, predecessor[v], cost, n)
        cost += 1

        if v < n:
            print(v, end=" ")

    return cost

def findLeastPathCost(graph, source, dest, n):
    discovered = [False] * 3 * n
    discovered[source] = True

    predecessor = [-1] * 3 * n

    q = deque()
    q.append(source)

    while q:
        current = q.popleft()

        if current == dest:
            print(f"The least cost path betweem {source} to {dest} is", end=" ")
            print("having cost ",  {printPath(predecessor, dest, -1, n)})

        for v in graph.adjList[current]:
            if not discovered[v]:
                q.append(v)
                discovered[v] = True
                predecessor[v] = current


if __name__ == '__main__':
    x = 1
    edges = [
        (0, 1, 3*x), (0, 4, 1*x), (1, 2, 1*x), (1, 3, 3*x),
        (1, 4, 1*x), (4, 2, 2*x), (4, 3, 1*x)
    ]

    n = 5
    source = 0 
    dest = 2

    graph = Graph(edges, n, x)

    findLeastPathCost(graph, source, dest, n)
