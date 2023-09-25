class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src,dest) in edges:
            self.adjList[src].append(dest)

class DisjointSet:
    parent = {}

    def makeSet(self, n):
        for i in range(n):
            self.parent[i] = i

    
    def find(self, k):
        if self.parent[k] == k:
            return k

        return self.find(self.parent[k])


    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y


def findCycle(graphm, n):
    ds = DisjointSet()
    ds.makeSet(n)

    for u in range(n):
        for v in graph.adjList[u]:
            x = ds.find(u)
            y = ds.find(v)

            if x == y:
                return True

            else:
                ds.union(x, y)

    return False

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
        (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
    ]

    n = 12

    graph = Graph(edges, n)

    if findCycle(graph, n):
        print("Cycle found")
    else:
        print('Cycle not found')